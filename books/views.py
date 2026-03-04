# books/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing books.
    Provides 'list', 'create', 'retrieve', 'update', 'partial_update', and 'destroy' actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer