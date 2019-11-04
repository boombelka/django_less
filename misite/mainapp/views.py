from django.shortcuts import render

# Create your views here.


def main(request):
    context = {
    'title': 'Главная',
    'username': 'иван'
    }
    return render(request, 'mainapp/main.html', context)


def products(request):
    context = {
        'title': 'Продукты',
        'products': ['Банан', 'Яблоко', 'Груша']
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html', {'title': 'Контакты'})