# import datetime # debug
import json
import scrapy
import uuid

valid_tags = [
    # region
    "Indonesian", "Chinese", "Filipino", "Indian", "Malaysian", "Thai", "Korean", "Japanese", "Singaporean", "Vietnamese", "Peranakan", "Middle-Eastern",

    # difficulty
    "Easy", "Medium", "Hard",

    # time
    "Above 60 mins", "Under 30 mins", "Under 45 mins", "Under 60 mins", "Under 15 mins"

    # meal
    "Lunch", "Dinner", "Breakfast", "Appetizers"

    # non_meal
    "Dessert", "Snacks", "Drinks", "Baked Goods", "Bread", "Salad", "Cake", "Cookies",

    # diet
    "Halal", "Vegetarian", "Keto", "Nonya", "Vegan", "Low Carb", "Greens", "Traditional", "Alcoholic",

    # flavor
    "Savory", "Spicy", "Sweet", "Fruity", "Sour", "Sweet and sour", "Mala",

    # holiday
    "Chinese New Year", "Hari Raya", "Ramadan", "Mid-Autumn Festival", "Christmas"

    # invalid
    "Malaysia", "Special Diets Keto"
]

class RecipeGetter():
    def __init__(self):
        self.start = self.end = uuid.uuid1().hex
        self.ids = [uuid.uuid1().hex, uuid.uuid1().hex, self.start]

    def warning(self):
        print(f'\n"next" of the last recipe should be changed to {self.start}')
        print(f'"prev" of the first recipe should be changed to {self.end}\n')
    
    def get(self, response):
        self.ids.pop(0)
        self.ids.append(uuid.uuid1().hex)
        self.end = self.ids[1]

        return {
            'prev': self.ids[0],
            'id': self.end,
            'next': self.ids[2],
            'title': self.get_title(response),
            'content': self.get_content(response),
            'image_url': self.get_image_url(response),
            'ingredients': self.get_ingredients(response),
            'instructions': self.get_instructions(response),
            'tags': self.get_tags(response),
            'time': self.get_time(response),
        }

    def get_title(self, response):
        return response.css("h2.cmp-title__text::text").get()

    def get_content(self, response):
        return response.css("div.m-content__copy").css("span::text").get()

    def get_image_url(self, response):
        return response.css("div.m-recipe-arrange").css("div.cmp-image").css("img").xpath("@data-src").get()

    def get_ingredients(self, response):
        # serving_size = response.css("div.m-recipeDetailList").css("li.m-recipeDetailList__item").css("strong::text").get()
        ingredients = response.css("div.m-recipeDetailList").css("li.m-recipeDetailList__item").css("p")
        return [{
            'content': i.css("::text").get() + (i.css("i::text").get() if i.css("i::text") else ""),
            'match': False,
        } for i in ingredients]

    def get_instructions(self, response):
        instructions = response.xpath(
            "//div[@class='o-ordered-listing']/div[@class='cmp-text']//div[@class='m-ordered-listing__item']")
        # for instruction in instructions:
        #     for step in filter(lambda step: step != "\n", instruction.xpath(".//div[@class='cmp-text']//text()").getall()):
        #         print(step)
        return [{
            'title': instruction.xpath(".//h3/text()").get(),
            'contents': [step for step in filter(lambda step: step != "\n", instruction.xpath(".//div[@class='cmp-text']//text()").getall())],
        } for instruction in instructions]

    def get_tags(self, response):
        difficulty = self.get_difficulty(response)
        categories = response.css("a.a-category-tag__title")
        tags = list(filter(lambda tag: tag in valid_tags and tag not in difficulty,
            [category.css("::text").get() for category in categories])) + difficulty
        return ['Malaysian' if tag == 'Malaysia' else tag for tag in
                ['Keto' if tag == 'Special Diets Keto' else tag for tag in tags]]
        

    def get_difficulty(self, response):
        return [response.xpath("//div[@class='m-recipe-overview__highlights desktop']//span/text()").getall()[0]]

    def get_time(self, response):
        overview = response.xpath("//div[@class='m-recipe-overview__highlights desktop']//span/text()").getall()
        return {
            'preparation': overview[1],
            'cook': overview[2],
            'cleanup': overview[3],
        }

class AfnSpider(scrapy.Spider):
    # init
    name = 'afn'
    recipe_getter = RecipeGetter()
    path2dir = './recipe_scraper/export'
    fp = open(f"{path2dir}/recipes.js", "w")
    # fp = open(f"{path2dir}/{datetime.date.today()}.json", "w") # debug
    url = 'https://asianfoodnetwork.com'
    extensions = set()
    start_extensions = [
        # with http error
        '/en/recipes/cuisine/thai/thai-twist-onsen-eggs.html',

        # without http error
        # '/en/recipes/ingredients/chicken/rice-cooker-chicken.html',
        # '/en/recipes/ingredients/vegetables/green-goddess-vegetable-pilaf.html',
        # '/en/recipes/ingredients/zucchini/zucchini-chips-with-nacho-dip.html',
        # '/en/recipes/ingredients/seafood/easy-to-cook-delicious-seafood-cheese-baked-rice.html',
        # '/en/recipes/ingredients/salted-egg/salted-egg-kale-chips.html',
        # '/en/recipes/ingredients/beef/curry-beef-cheesy-tacos.html',
        # '/en/recipes/ingredients/fish/pan-fried-red-tilapia-with-tomato-and-gac-fruit-sauce.html',

        # '/en/recipes/cuisine/korean/kimchi-grilled-cheese.html',
        # '/en/recipes/cuisine/malaysian/Mango-Yoghurt-Curry.html',
        # '/en/recipes/cuisine/peranakan/chicken-pongteh.html',
        # '/en/recipes/cuisine/chinese/white-seafood-lor-mee.html',
        # '/en/recipes/cuisine/indonesian/garang-asem.html',
        # '/en/recipes/cuisine/singaporean/vegetarian-peranakan-laksa.html',
        # '/en/recipes/cuisine/indian/vegetarian-briyani.html',
        # '/en/recipes/cuisine/japanese/takoyaki.html',
        # '/en/recipes/cuisine/asian-desserts/old-fashioned-donut-rings.html',
        # '/en/recipes/cuisine/filipino/Pork-Pata-Kare-Kare.html',
        # '/en/recipes/cuisine/vietnamese/vietnamese-fresh-spring-rolls.html',
    ]

    # override
    def start_requests(self):
        self.fp.write('const recipes = [\n')
        yield scrapy.Request(url=f'{self.url}{self.start_extensions[0]}', meta={'handle_httpstatus_all': True}, dont_filter=True)

    def parse(self, response):
        OK, extension = response.status in [200], response.url[len(self.url):]
        if OK and extension not in self.extensions:
            recipe = self.recipe_getter.get(response)

            self.fp.write(',\n' if len(self.extensions) else '')
            json.dump(recipe, self.fp, indent=4)

            self.extensions.add(extension)
            extension = response.xpath("//div[@class='col-md-6 col-6 m-default-pagination-img__next p-0']//a/@href").get()
        else:
            if OK:
                print(f'Hit {extension}')
            self.start_extensions.pop(0)
            if len(self.start_extensions):
                extension = self.start_extensions[0]
            else:
                self.fp.write('];\n\nexport default recipes;')
                self.recipe_getter.warning()
                self.fp.close()
                return
        yield scrapy.Request(url=f'{self.url}{extension}', meta={'handle_httpstatus_all': True}, dont_filter=True)

    # def parse_region(self, response):
    #     # regions = response.css("a.a-linked-image").xpath("@href").getall()
    #     regions = [str[len("/en/recipes/cuisine/"):-len(".html")] for str in response.css("a.a-linked-image").xpath("@href").getall()]
    #     print(regions)
