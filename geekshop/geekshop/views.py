from django.shortcuts import render
from mainapp.models import Product

# def index(request):  # original
#     return render(request, 'geekshop/index.html')


def index(request):  # not original
    products = Product.objects.all()[:4]

    context = {
        'title': 'главная',
        'products': products,
    }


    return render(request, 'geekshop/index.html', context)



def contacts(request):
    return render(request, 'geekshop/contact.html')