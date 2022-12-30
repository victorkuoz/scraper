# scraper

## scrapy
### usage
```
git clone https://github.com/victorkuoz/scraper.git
cd scraper
scrapy crawl afn
```

### example output
- https://asianfoodnetwork.com/en/recipes/cuisine/thai/thai-twist-onsen-eggs.html
```
"id": "908b26ac87ef11eda55847b92c10f584",
    "title": "Thai Twist Onsen Eggs",
    "content": "We all know the flavourful shoyu-based onsen tamago, but here\u2019s one perfumed with heady Thai flavours of sprity lemongrass and gingery galangal, crisp fried shallots, Thai chillies and coriander. Salty fish sauce, lightly sweetened with earthy palm sugar forms the broth of this refreshing infusion and pulls the whole thing together. Our way of eating it? Slice the soft-boiled egg in half and first plop in the jammy yolk, tongue down for a creamy mouthfeel, then sip on the broth and repeat for the other half \u2013 this way you get to taste this twice! ",
    "image_url": "https://asianfoodnetwork.com/content/dam/afn/global/en/recipes/thai-twist-onsen-egg/Thai_Twist_Onsen_Tamago_Sauce_article_1920x1280_7.jpg.transform/recipestep-img/img.jpg",
    "ingredients": [
        "4 large-sized eggs (keep cold and refrigerated till needed)",
        "1 liter + 150ml of cool water",
        "\u00a0",
        "For the sauce:",
        "150ml water",
        "1 tbsp fish sauce",
        "\u00bc inch piece galangal, peeled",
        "1 lemongrass, outer leaves trimmed",
        "2 kaffir lime leaves",
        "1 red bird\u2019s eye chili",
        "1 tsp palm sugar",
        "\u00a0",
        "Garnish:",
        "1 tbsp fried shallots",
        "1 sprig coriander",
        "1 red bird\u2019s eye chili, sliced",
        "\u00a0"
    ],
    "instructions": [
        {
            "title": "Cook The Egg",
            "content": [
                "Put the 1 liter of water in a medium lidded pot and bring to a boil.",
                "When boiling, turn off the heat, add the 200ml of cool water.",
                "Gently add the cold eggs and cover, leaving for 18 minutes."
            ]
        },
        {
            "title": "Make The Broth",
            "content": [
                "While the eggs are cooking, make the broth.",
                "Bash the galangal and lemongrass, tear the kaffir lime leaves and slice the chili thinly.",
                "Add galangal, lemongrass and kaffir lime leaves to a small pot with 150ml of water and bring to a gentle simmer for 10 minutes.",
                "Add the chili, palm sugar and fish sauce, stir and turn off the heat, allowing this to cool completely."
            ]
        }
    ],
    "tags": [
        "Thai",
        "Egg"
    ],
    "difficulty": "Easy",
    "time": {
        "preparation": "5 min",
        "cook": "30 min",
        "cleanup": "5 min"
    }
}
```

## extractor
### raw tags
```
'Thai', 'Egg', 'Rice', 'Seafood', 'Under 30 mins', 'Sweet and sour', 'Easy', 'Prawn', 'Noodles', 'Savory', 'Snacks', 'Chicken', 'Fish', 'Spicy', 'Vegetables', 'Garlic', 'Pork', 'Sweet', 'Medium', 'Coconut milk', 'Salad', 'Soybean', 'Galangal', 'Flour', 'Butter', 'Dessert', 'Lunch', 'Beef', 'Sour', 'Dinner', 'Fruity', 'Appetizers', 'Chinese', 'Bitter Melon', 'Hard', 'Low Carb', 'Vietnamese', 'Under 60 mins', 'Breakfast', 'Halal', 'Chilli', 'Under 45 mins', 'Above 60 mins', 'Cheese', 'Article', 'Video', 'Mushroom', 'Japanese', 'Pasta', 'Fruits', 'Milk', 'Nuts', 'Tofu', 'Zucchini', 'Vegetarian', 'Series', 'Keto', 'Mala', 'Middle-Eastern', 'Hari Raya', 'Sweet Potato', 'Indian', 'Special Diets Keto', 'Alcoholic', 'Chocolate', 'Chinese New Year', 'Avocado', 'Potatoes', 'Under 15 mins', 'Baked Goods', 'Bread', 'Vegan', 'Special Diets Gluten Free', 'Ingredients', 'Singaporean', 'Salted Egg', 'Lamb', 'Malaysian', 'Minced', 'Korean', 'Indonesian', 'Nonya', 'Kale', 'Malaysia', 'Gula Melaka', 'Ramadan', 'Pandan', 'Mid-Autumn Festival', 'Duck', 'Greens', 'Traditional', 'Yam', 'Rambutan', 'Chicken liver', 'Drinks', 'Jackfruit', 'Honey', 'Salted Fish', 'Tempeh', 'Coconut', 'Singapore', 'Cauliflower', 'How To', 'Matthias Rhoads', 'Cake', 'Cookies', 'Pudding', 'Philippines', 'Filipino', 'Gluten-free', 'Special Diets Low Carb', 'Brunch', 'Main Dish', 'Peanut', 'Kimchi', 'Mexican', 'Christmas', 'Flourless'
```

### raw ingredients
- (keyword, # of appearance)
```
('g', 7687), ('tbsp', 2240), ('tsp', 1943), ('ml', 1659), ('water', 1090), ('oil', 1081), ..., ('oelek', 1), ('Julienne', 1), ('sizes', 1), ('elephant', 1), ('paddy', 1), ('corianders', 1)
```