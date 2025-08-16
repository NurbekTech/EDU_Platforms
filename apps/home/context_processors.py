# apps/home/context_processors.py
def menu_items(request):
    return {
        "menu_items": [
            {"name": "Главная", "url_name": "home"},
            {"name": "Блог", "url_name": "blog"},
        ]
    }
