from django.urls import path
from .views import Author, Stack
from django.contrib import admin
urlpatterns = [
    path('/about/author/', views.Author.as_view()),

]