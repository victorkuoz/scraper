import json
import scrapy

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
        #     for step in instruction.xpath(".//div[@class='cmp-text']//p | .//div[@class='cmp-text']//li"):
        #         print (step.css("::text").get() + (step.xpath("./i/text()").get() if step.xpath("./i") else ""))
        return [{
            'title': instruction.xpath(".//h3/text()").get(),
            'content': [step.css("::text").get() + (step.xpath("./i/text()").get() if step.xpath("./i") else "")
                for step in instruction.xpath(".//div[@class='cmp-text']//p | .//div[@class='cmp-text']//li")],
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

class AfnSpider(scrapy.Spider):
    allowed_domains = ['www.asianfoodnetwork.com']
    base_url = "https://asianfoodnetwork.com"
    name = 'afn'
    start_urls = []

    # unnecessary
    '''
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
    '''

    # overrided
    def start_requests(self):
        # print("start_requests")

        yield scrapy.Request(
            url=self.base_url+"/en/recipes/cuisine/chinese/chinese-style-scrambled-eggs-with-tomato.html", callback=self.parse_recipe)

        # genres = ["cuisine", "ingredients", "special-diets"]
        yield scrapy.Request(url=self.base_url+"/en/recipes/cuisine.html", callback=self.parse_region)

    # deprecated
    '''
    def parse(self, response):
        pass
    '''

    def parse_recipe(self, response):
        # print("parse_recipe")
        recipe = RecipeGetter().get(response)
        print(json.dumps(recipe, indent=4))

    def parse_region(self, response):
        # print("parse_region")
        regions = [str[len("/en/recipes/cuisine/"):-len(".html")] for str in response.css("a.a-linked-image").xpath("@href").getall()]
        print(regions)