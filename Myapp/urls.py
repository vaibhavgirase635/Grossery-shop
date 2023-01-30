from django.urls import path
from Myapp import views

urlpatterns = [
    path('login/', views.LoginPage,name='login'),
    path('signup/', views.SignupPage,name='signup'),
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('checkout/', views.checkout,name='checkout'),
    path('contact/', views.contact,name='contact'),
    path('faqs/', views.faqs,name='faqs'),
    path('help/', views.help,name='help'),
    path('icons/', views.icons,name='icons'),
    path('payment/', views.payment,name='payment'),
    path('privacy/', views.privacy,name='privacy'),
    path('product/', views.product,name='product'),
    path('product2/', views.product2,name='product2'),
    path('single/', views.single,name='single'),
    path('single2/', views.single2,name='single2'),
    path('terms/', views.terms,name='terms'),
    path('typography/', views.typography,name='typography'),

]