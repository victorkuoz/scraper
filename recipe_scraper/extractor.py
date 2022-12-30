import json
import re

path2dir = './export'

with open(f'{path2dir}/recipes.json', 'r') as rf:
    recipes = json.load(rf)

    # tags
    tag_dict = dict()
    for recipe in recipes:
        for tag in recipe['tags']:
            if tag in tag_dict.keys():
                tag_dict[tag]+=1
            else:
                tag_dict[tag]=1
    tags = sorted(tag_dict.items(), key=(lambda tag: tag[1]), reverse=True)
    with open(f'{path2dir}/raw_tags', 'w') as wf:
        for tag in tags:
            wf.write(f'{tag}\n')
    
    # ingredients
    ingredient_dict = dict()
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            for voc in re.findall('[a-zA-Z]+', ingredient):
                if voc.lower() in ingredient_dict.keys():
                    ingredient_dict[voc.lower()]+=1
                else:
                    ingredient_dict[voc.lower()]=1
    ingredients = sorted(ingredient_dict.items(), key=(lambda ingredient: ingredient[1]), reverse=True)
    with open(f'{path2dir}/raw_ingredients', 'w') as wf:
        for ingredient in ingredients:
            wf.write(f'{ingredient}\n')
