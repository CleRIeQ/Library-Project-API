from rest_framework import generics
from library.models import Book
from .serializers import BookSerializer

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
