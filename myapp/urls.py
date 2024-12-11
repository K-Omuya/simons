from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('track/', views.track, name='track'),
    path('categories/', views.categories, name='categories'),

    path('', views.register, name='register'),


    path('login/', views.login, name='login'),
]
