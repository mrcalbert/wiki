from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entries, name="entries"),
    path("search", views.searchbar, name="searchbar"),
    path("newpage", views.newpage, name="newpage"),
    path("editpage", views.edit, name="editpage"),
    path("random", views.randompage, name="randompage"),
]
