
from django.urls import path
from .views import products

app_name = 'mainapp'


urlpatterns = [
    path('', products, name='index'),
    # path('<int:pk>/', product, name='product')
]