from django.shortcuts import render
from .serializers import CategorySerializer, ArticleSerializer
from blogapp.models import CategoryClass, Article
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]

class ArticleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Article.objects.all()
    serializer_class = ArticleSerializer

class ArticlesInCategoryListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        category = self.kwargs['category']
        try:
            return Article.objects.filter(category = CategoryClass.objects.get(category = category).pk)
        except CategoryClass.DoesNotExist:
            raise Http404("No such category exist.")