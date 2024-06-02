from rest_framework import serializers
from blogapp.models import CategoryClass
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryClass
        fields='__all__'