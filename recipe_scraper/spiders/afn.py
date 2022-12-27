import json
import scrapy

def get_title(response):
    return response.css("h2.cmp-title__text::text").get()

def get_content(response):
    return response.css("div.m-content__copy").css("span::text").get()

def get_image(response):
    return response.css("div.m-recipe-arrange").css("div.cmp-image").css("img").xpath("@data-src").get()

def get_ingredients(response):
    # serving_size = response.css("div.m-recipeDetailList").css("li.m-recipeDetailList__item").css("strong::text").get()
    ingredients = response.css("div.m-recipeDetailList").css("li.m-recipeDetailList__item").css("p")
    return [i.css("::text").get() + (i.css("i::text").get() if i.css("i::text") else "") for i in ingredients]

def get_instructions(response):
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

def get_categories(response):
    categories = response.css("a.a-category-tag__title")
    return list(filter(lambda category: category != 'Recipe', [category.css("::text").get() for category in categories]))

def get_overview(response):
    overview = response.xpath("//div[@class='m-recipe-overview__highlights desktop']//span/text()").getall()
    return {
        'difficulty': overview[0],
        'time': {
            'preparation': overview[1],
            'cook': overview[2],
            'cleanup': overview[3],
        },
    }

def get_recipe(response):
    recipe = {
        # 'id':
        'title': get_title(response),
        'content': get_content(response),
        'image': get_image(response),
        'ingredients': get_ingredients(response),
        'instructions': get_instructions(response),
        'categories': get_categories(response),
        'overview': get_overview(response),
        # 'arrange'
    }
    print(json.dumps(recipe, indent=4))
    return recipe

class AfnSpider(scrapy.Spider):
    name = 'afn'
    allowed_domains = ['www.asianfoodnetwork.com']
    # start_urls = ['http://www.asianfoodnetwork.com/']
    start_urls = [
        "https://asianfoodnetwork.com/en/recipes/cuisine/chinese/chinese-style-scrambled-eggs-with-tomato.html",
    ]

    def parse(self, response):
        recipe = get_recipe(response)
        
