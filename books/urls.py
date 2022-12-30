import books.views
from django.urls import path

urlpatterns = [
    path('books/add/', books.views.AddBook.as_view(), name="add-book"),
    path('books/', books.views.BookListView.as_view(), name="books"),
    path('books/<int:pk>/', books.views.BookDetailView.as_view(), name="book-detail"),
    path('authors/', books.views.AuthorView.as_view(), name="authors"),
    path('categories/', books.views.CategoryView.as_view(), name="categories"),
]
