from django.urls import path
from .views import search_chunks

urlpatterns = [
    path("search/", search_chunks, name="search_chunks"),
]
