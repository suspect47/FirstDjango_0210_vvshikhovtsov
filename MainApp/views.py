from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"

}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
    # text = """<h1>"Изучаем django"</h1>
    #           <strong>Автор</strong>: <i>Шиховцов В.В.</i>
    #        """
    # return HttpResponse(text)
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@example.com"
    }
    return render(request, "index.html", context)


def about(request):
    result = f"""
    <header>
        /<a href="/">Home</a> / <a href="/items"> Items</a> / <a href="/about"> About</a>
    </header><br>
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(result)


def get_item(request, item_id):
    """ По указанному id возвращает имя и количество """
    # for item in items:
    #     if item["id"] == id:
    #         result = f"""
    #         <h2>Имя: {item["name"]} </h2>
    #         <p>Количество: {item["quantity"]} </p>
    #         <p><a href="/items"> Назад к списку товаров </a></p>
    #         """
    #         return HttpResponse(result)
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        context = {
            "item": item
        }
        return render(request, "item-page.html", context)
    return HttpResponseNotFound(f'Item with id={id} not found')


def items_list(request):
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)