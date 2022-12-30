import json

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class AuthorView(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddBook(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        #if(request.)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListView(APIView):

    def get(self, request, format=None):
        name = request.GET.get("name")
        books = Book.books_manager.get_queryset()
        if name != "":
            books = books.filter(name=name)
        if request.GET.get("author") != "":
            author = request.GET.get("author")
            author = [int(x.strip()) for x in author.split(',') if x]
            books = books.filter(author__in=author)
        if request.GET.get("category") != "":
            category = request.GET.get("category")
            category = [int(x.strip()) for x in category.split(',') if x]
            books = books.filter(category__in=category)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):

    def get(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'Message: Book doesn\'t exist'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({'Message: Book doesn\'t exist'}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({'Message: Book is deleted'}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'Message: Book doesn\'t exist'}, status=status.HTTP_204_NO_CONTENT)


