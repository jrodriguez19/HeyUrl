from django.urls import path

from heyurl import views

urlpatterns = [
    path('', views.short_url, name='short_url'),
    path('chart/', views.statistics, name='statistics'),
]
