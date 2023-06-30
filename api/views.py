from django.shortcuts import render
from rest_framework.generics import ListAPIView

from books.models import Book, Tag
from .serializers import BookSerializer, TagSerializer


class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



