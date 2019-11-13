from django.shortcuts import render
from .models import ProductCategory, Product
from django.views.generic.edit import UpdateView

# Create your views here.
def main(request):
    return render(request, 'mainapp/main.html')

def products(request):
    return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

# Аутентификация пользователей методы

def register(request):
    pass

def login(request):
    return render(request, 'authapp/login.html')

def logout(request):
    pass

class EditView(UpdateView):
    pass