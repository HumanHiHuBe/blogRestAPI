from django.urls import path
from blogRestAPI import views

urlpatterns = [
    path('categorylist/', views.CategoryListView.as_view()),
    path('auth/', views.CategoryListView.as_view()),
] 
