# apps/home/context_processors.py
def menu_items(request):
    return {
        "menu_items": [
            {"name": "Блог", "url_name": "blog"},
            {"name": "Контакты", "url_name": "home_contacts"},
        ]
    }
