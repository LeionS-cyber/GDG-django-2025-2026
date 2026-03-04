# books/serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # Include all fields from the Book model
        # You can specify individual fields like:
        # fields = ['id', 'title', 'author', 'isbn', 'publication_date', 'price']
        read_only_fields = ['created_at', 'updated_at'] # These fields are automatically set by Django