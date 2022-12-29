import datetime
import json
import scrapy
from scrapy_selenium import SeleniumRequest

class RecipeGetter():
    def get(self, response):
        return {
            # 'id':
            'title': self.get_title(response),
            'content': self.get_content(response),
            'image': self.get_image(response),
            'ingredients': self.get_ingredients(response),
            'instructions': self.get_instructions(response),
            'tags': self.get_tags(response),
            'overview': self.get_overview(response),
            # 'arrange'
        }

    def get_title(self, response):
        return response.css("h2.cmp-title__text::text").get()

    def get_content(self, response):
        return response.css("div.m-content__copy").css("span::text").get()

    def get_image(self, response):
        return response.css("div.m-recipe-arrange").css("div.cmp-image").css("img").xpath("@data-src").get()

    def get_ingredients(self, response):
        # serving_size = response.css("div.m-recipeDetailList").css("li.m-recipeDetailList__item").css("strong::text").get()
        ingredients = response.css("div.m-recipeDetailList").css("li.m-recipeDetailList__item").css("p")
        return [i.css("::text").get() + (i.css("i::text").get() if i.css("i::text") else "") for i in ingredients]

    def get_instructions(self, response):
        instructions = response.xpath(
            "//div[@class='o-ordered-listing']/div[@class='cmp-text']//div[@class='m-ordered-listing__item']")
        # for instruction in instructions:
        #     for step in filter(lambda step: step != "\n", instruction.xpath(".//div[@class='cmp-text']//text()").getall()):
        #         print(step)
        return [{
            'title': instruction.xpath(".//h3/text()").get(),
            'content': [step for step in filter(lambda step: step != "\n", instruction.xpath(".//div[@class='cmp-text']//text()").getall())],
        } for instruction in instructions]

    def get_tags(self, response):
        categories = response.css("a.a-category-tag__title")
        return list(filter(lambda category: category != 'Recipe', [category.css("::text").get() for category in categories]))

    def get_overview(self, response):
        overview = response.xpath("//div[@class='m-recipe-overview__highlights desktop']//span/text()").getall()
        return {
            'difficulty': overview[0],
            'time': {
                'preparation': overview[1],
                'cook': overview[2],
                'cleanup': overview[3],
            },
        }

# global
base_url = 'https://asianfoodnetwork.com'
extensions = set()
fp = open(f"./recipe_scraper/export/{datetime.date.today()}.json", "w")
threshold = 3

class AfnSpider(scrapy.Spider):
    # /en/recipes/cuisine/chinese/chinese-style-scrambled-eggs-with-tomato.html
    name = 'afn'

    # override
    def start_requests(self):
        fp.write('[')
        extension = '/en/recipes/cuisine/chinese/white-seafood-lor-mee.html'
        yield SeleniumRequest(url=(base_url + extension), meta={'cnt': 0}, callback=self.parse_recipe, dont_filter=True)

    # self-define
    def parse_recipe(self, response):
        print(response.meta['cnt'])
        if response.meta['cnt'] < threshold:
            extension = response.url[len(base_url):]
            if extension not in extensions:
                recipe = RecipeGetter().get(response)
                fp.write(f"{',' if len(extensions) else ''}")
                json.dump(recipe, fp, indent=4) # print(json.dumps(recipe, indent=4))
                extensions.add(extension)
            else:
                print(f'Hit {response.url[len(base_url):]}')

            extension = response.xpath("//div[@class='col-md-6 col-6 m-default-pagination-img__next p-0']//a/@href").get()
            if not extension:
                print('No next page')
            else: 
                yield SeleniumRequest(url=(base_url + extension),
                    meta={'cnt': response.meta['cnt'] + 1}, callback=self.parse_recipe, dont_filter=True)
        else:
            fp.write(']')
            fp.close()

    def parse_region(self, response):
        # regions = response.css("a.a-linked-image").xpath("@href").getall()
        regions = [str[len("/en/recipes/cuisine/"):-len(".html")] for str in response.css("a.a-linked-image").xpath("@href").getall()]
        print(regions)
    
    # # unnecessary
    # def __init__(self, name=None, **kwargs):
    #     super().__init__(name, **kwargs)

    # # deprecate
    # def parse(self, response):
    #     pass