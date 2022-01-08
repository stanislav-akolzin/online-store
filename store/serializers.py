from rest_framework import serializers
from .models import Item, ItemCategory, ItemChange
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    '''Serializer for User model'''
    class Meta:
        model = User
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    '''Serializer for items list show, creating and updating items'''
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'quantity']

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        item = instance[0]
        item.name = validated_data.get('name', item.name)
        item.category = validated_data.get('category', item.category)
        item.description = validated_data.get('description', item.description)
        item.price = validated_data.get('price', item.price)
        item.quantity = validated_data.get('quantity', item.quantity)
        item.save()

        return instance


class CategorySerializer(serializers.Serializer):
    '''Serializer for categories list'''
    name = serializers.CharField()
    description = serializers.CharField()
    item_quantity = serializers.IntegerField(source='count_items')


class CategoryActionsSerializer(serializers.Serializer):
    '''Serializer for creating and updating categories'''
    name = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        return ItemCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        category = instance[0]
        category.name = validated_data.get('name', category.name)
        category.description = validated_data.get('description', category.description)
        category.save()
        return instance


class ItemSerializer(serializers.Serializer):
    '''Serializer for detailed item information'''
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    changes = serializers.ListField(source='item_changes')