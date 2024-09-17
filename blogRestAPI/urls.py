from django.urls import path
from blogRestAPI import views

urlpatterns = [
    path('categorylist/', views.CategoryListView.as_view()),
    path('categorylist/<int:pk>', views.CategoryDetailsView.as_view()),
    path('articlelist/', views.ArticleListView.as_view()),
    path('articlelist/<int:pk>', views.ArticleDetailsView.as_view()),
    path('articleincategorylist/<str:category>', views.ArticlesInCategoryListView.as_view()),
] 
