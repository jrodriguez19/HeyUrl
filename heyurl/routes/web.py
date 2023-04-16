from django.urls import path

from heyurl import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store', views.store, name='store'),
]
