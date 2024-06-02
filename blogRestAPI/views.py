from django.shortcuts import render
from .serializers import CategorySerializer
from blogapp.models import CategoryClass
from rest_framework import generics
# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset= CategoryClass.objects.all()
    serializer_class = CategorySerializer