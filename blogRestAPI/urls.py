from django.urls import path
from blogRestAPI import views

urlpatterns = [
    path('categorylist/', views.CategoryListView.as_view())
] 
