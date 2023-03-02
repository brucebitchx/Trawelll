from django.urls import path, include
import base.views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
    path('deals/', views.deals, name='deals'),
]
