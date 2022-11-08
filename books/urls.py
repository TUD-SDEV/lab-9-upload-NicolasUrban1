from django.urls import URLPattern, path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

URLPatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
]