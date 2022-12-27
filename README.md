# scraper

### run
```
git clone https://github.com/victorkuoz/scraper.git
cd scraper
scrapy crawl afn
```

### example recipe output
- https://asianfoodnetwork.com/en/recipes/cuisine/chinese/chinese-style-scrambled-eggs-with-tomato.html
```
{
    "title": "Chinese Style Scrambled Eggs with Tomato",
    "content": "This comforting dish of scrambled eggs features the natural sweetness of bright red tomatoes and is an easy-to-make side dish for any dinner table!",
    "image": "https://asianfoodnetwork.com/content/dam/afn/global/en/recipes/chinese-style-scrambled-eggs/AFN_chinese_style_scrambled_eggs_with_tomato_main_image.jpg.transform/recipestep-img/img.jpg",
    "ingredients": [
        "4 eggs (beaten)",
        "1 medium tomato (cut into pieces)",
        "2 spring onion",
        "1 tsp ginger (sliced)",
        "2 stalks coriander (roughly chopped)",
        "2 tsp chili sauce (subsitute with sriracha sauce)",
        "1 tbsp vegetable oil",
        "2 tsp salt"
    ],
    "instructions": [
        {
            "title": " Stir-fry spring onion and ginger",
            "content": [
                "In a hot pan, add 1 tbsp vegetable oil, spring onion and sliced ginger. Fry for 15 seconds."
            ]
        },
        {
            "title": "Stir-fry tomatoes and egg",
            "content": [
                "Add tomato and stir fry for 1 min or until slightly soft.",
                "Add 4 beaten eggs and 2 tsp of salt. Stir fry until eggs are cooked.",
                "| This dish is best eaten as a side dish with steamed white rice"
            ]
        }
    ],
    "categories": [
        "Chinese",
        "Easy",
        "Under 15 mins",
        "Vegetables",
        "Halal"
    ],
    "overview": {
        "difficulty": "Easy",
        "time": {
            "preparation": "10 min",
            "cook": "5 min",
            "cleanup": "10 min"
        }
    }
}
```