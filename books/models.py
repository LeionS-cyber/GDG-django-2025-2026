# books/models.py

from django.db import models
from django.core.validators import MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, help_text="International Standard Book Number")
    publication_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title'] # Default ordering for books

    def __str__(self):
        return f"{self.title} by {self.author}"