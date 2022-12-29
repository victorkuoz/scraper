import json
import re

path2dir = './export'

with open(f'{path2dir}/recipes.json', 'r') as rf:
    recipes = json.load(rf)

    # tags
    tags = set()
    for recipe in recipes:
        for tag in recipe['tags']:
            tags.add(tag)
    with open(f'{path2dir}/tags.txt', 'w') as wf:
        for tag in tags:
            wf.write(f'{tag}\n')
    
    # ingredients
    ingredients = dict()
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            for key in re.findall('[a-zA-Z]+', ingredient):
                if key in ingredients.keys():
                    ingredients[key]+=1
                else:
                    ingredients[key]=1
    ingredients = sorted(ingredients.items(), key=(lambda ingredient: ingredient[1]), reverse=True)
    with open(f'{path2dir}/ingredients.txt', 'w') as wf:
        for ingredient in ingredients:
            wf.write(f'{ingredient}\n')
