from django.shortcuts import render
from .serializers import CategorySerializer, ArticleSerializer
from blogapp.models import CategoryClass, Article
from rest_framework import generics
# Create your views here.

class CategoryListView(generics.ListCreateAPIView):
    queryset= CategoryClass.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset= CategoryClass.objects.all()
    serializer_class = CategorySerializer

class ArticleListView(generics.ListCreateAPIView):
    queryset= Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleListView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Article.objects.all()
    serializer_class = ArticleSerializer

class ArticlesInCategoryListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        category = self.kwargs['category']
        return Article.objects.filter(category = CategoryClass.objects.get(category = category).pk)