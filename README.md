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
('Easy', 786), ('Vegetables', 532), ('Indonesian', 463), ('Above 60 mins', 373), ('Dessert', 359), ..., ('Brunch', 1), ('Peanut', 1), ('Kimchi', 1), ('Mexican', 1), ('Flourless', 1)
```

### raw ingredients
- (keyword, # of appearance)
```
('g', 7688), ('tbsp', 2255), ('tsp', 1949), ('ml', 1680), ('salt', 1261), ..., ('oelek', 1), ('sizes', 1), ('elephant', 1), ('paddy', 1), ('corianders', 1)
```