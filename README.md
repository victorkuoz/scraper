# scraper

## scrapy
### usage
```
git clone https://github.com/victorkuoz/scraper.git
cd scraper
scrapy crawl afn
```
### note the warning message in terminal
```
"next" of the last recipe should be changed to ...
"prev" of the first recipe should be changed to ...
```

### example output
- https://asianfoodnetwork.com/en/recipes/cuisine/thai/thai-twist-onsen-eggs.html
```
{
    "prev": "1f7d48b98aa911eda9ecf19f891c3f45",
    "id": "1541262e8aa911eda9ecf19f891c3f45",
    "next": "154126318aa911eda9ecf19f891c3f45",
    "title": "Thai Twist Onsen Eggs",
    "content": "We all know the flavourful shoyu-based onsen tamago, but here\u2019s one perfumed with heady Thai flavours of sprity lemongrass and gingery galangal, crisp fried shallots, Thai chillies and coriander. Salty fish sauce, lightly sweetened with earthy palm sugar forms the broth of this refreshing infusion and pulls the whole thing together. Our way of eating it? Slice the soft-boiled egg in half and first plop in the jammy yolk, tongue down for a creamy mouthfeel, then sip on the broth and repeat for the other half \u2013 this way you get to taste this twice! ",
    "image_url": "https://asianfoodnetwork.com/content/dam/afn/global/en/recipes/thai-twist-onsen-egg/Thai_Twist_Onsen_Tamago_Sauce_article_1920x1280_7.jpg.transform/recipestep-img/img.jpg",
    "ingredients": [
        {
            "content": "4 large-sized eggs (keep cold and refrigerated till needed)",
            "match": false
        },
        {
            "content": "1 liter + 150ml of cool water",
            "match": false
        },
        {
            "content": "\u00a0",
            "match": false
        },
        {
            "content": "For the sauce:",
            "match": false
        },
        {
            "content": "150ml water",
            "match": false
        },
        {
            "content": "1 tbsp fish sauce",
            "match": false
        },
        {
            "content": "\u00bc inch piece galangal, peeled",
            "match": false
        },
        {
            "content": "1 lemongrass, outer leaves trimmed",
            "match": false
        },
        {
            "content": "2 kaffir lime leaves",
            "match": false
        },
        {
            "content": "1 red bird\u2019s eye chili",
            "match": false
        },
        {
            "content": "1 tsp palm sugar",
            "match": false
        },
        {
            "content": "\u00a0",
            "match": false
        },
        {
            "content": "Garnish:",
            "match": false
        },
        {
            "content": "1 tbsp fried shallots",
            "match": false
        },
        {
            "content": "1 sprig coriander",
            "match": false
        },
        {
            "content": "1 red bird\u2019s eye chili, sliced",
            "match": false
        },
        {
            "content": "\u00a0",
            "match": false
        }
    ],
    "instructions": [
        {
            "title": "Cook The Egg",
            "contents": [
                "Put the 1 liter of water in a medium lidded pot and bring to a boil.",
                "When boiling, turn off the heat, add the 200ml of cool water.",
                "Gently add the cold eggs and cover, leaving for 18 minutes."
            ]
        },
        {
            "title": "Make The Broth",
            "contents": [
                "While the eggs are cooking, make the broth.",
                "Bash the galangal and lemongrass, tear the kaffir lime leaves and slice the chili thinly.",
                "Add galangal, lemongrass and kaffir lime leaves to a small pot with 150ml of water and bring to a gentle simmer for 10 minutes.",
                "Add the chili, palm sugar and fish sauce, stir and turn off the heat, allowing this to cool completely."
            ]
        }
    ],
    "tags": [
        "Thai",
        "Easy"
    ],
    "time": {
        "preparation": "5 min",
        "cook": "30 min",
        "cleanup": "5 min"
    }
}
```