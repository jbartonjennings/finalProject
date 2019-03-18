from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('beertypes/', views.beertypes, name='beertypes'),
    path('getproducts/', views.getproducts, name='getproducts'),
    path('productdetail/<int:id>', views.productdetail, name='details'),
    path('newProduct/', views.newProduct, name='newproduct'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]