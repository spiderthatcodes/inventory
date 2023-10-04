from django.urls import path
from .api_views import list_or_add_books, show_delete_edit_book

urlpatterns = [
    path('books/', list_or_add_books, name="list_or_add_books"),
    path('book/<int:id>/', show_delete_edit_book, name="show_delete_edit_book")
]
