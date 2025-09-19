from rest_framework import serializers
from .models import Product, Order


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'slug', 'title', 'price', 'image', 'section']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'slug', 'title',
                  'description', 'price', 'image', 'section']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'customer_name', 'customer_phone', 'comment']

    def create(self, validated_data):
        product = validated_data['product']
        validated_data['price_locked'] = product.price
        return super().create(validated_data)
