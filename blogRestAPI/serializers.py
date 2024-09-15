from rest_framework import serializers
from blogapp.models import CategoryClass, Article
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryClass
        fields='__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'