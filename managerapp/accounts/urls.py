from django.urls import path

from . import views # import view will not work & from .views import home as accounts-home can be done too

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),

]