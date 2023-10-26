from rest_framework import serializers
from .models import Product, Category
from django.contrib.auth.models import User



class ProductSerializer(serializers.ModelSerializer):
    by = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_by(self, obj):
        return obj.by.username

    def get_category(self, obj):
        return obj.category.name