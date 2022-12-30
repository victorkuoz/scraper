import json
import re

path2dir = './export'

with open(f'{path2dir}/recipes.json', 'r') as rf:
    recipes = json.load(rf)

    # tags
    tag_set = set()
    for recipe in recipes:
        for tag in recipe['tags']:
            tag_set.add(tag)
    with open(f'{path2dir}/raw_tags.txt', 'w') as wf:
        for tag in tag_set:
            wf.write(f'{tag}\n')
    
    # ingredients
    ingredient_dict = dict()
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            for voc in re.findall('[a-zA-Z]+', ingredient):
                if voc in ingredient_dict.keys():
                    ingredient_dict[voc]+=1
                else:
                    ingredient_dict[voc]=1
    ingredients = sorted(ingredient_dict.items(), key=(lambda ingredient: ingredient[1]), reverse=True)
    with open(f'{path2dir}/raw_ingredients.txt', 'w') as wf:
        for ingredient in ingredients:
            wf.write(f'{ingredient}\n')
