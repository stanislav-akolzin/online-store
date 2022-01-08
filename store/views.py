from django.views.decorators.csrf import csrf_exempt
from .models import ItemCategory, Item, ItemChange
from rest_framework import generics
from . import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR
)


class TenItemsPagination(PageNumberPagination):
    '''Pagination in REST api'''
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class ItemList(generics.ListAPIView):
    '''Items with no category filter. Paginator is used.'''
    permission_classes = ([AllowAny])

    queryset = Item.objects.all().order_by('category', 'name')
    serializer_class = serializers.ItemsSerializer
    pagination_class = TenItemsPagination


class ItemDetail(generics.RetrieveAPIView):
    '''Detailed information for item and the history of item's changes'''
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer


class CategoryList(generics.ListAPIView):
    '''All categories'''

    def get(self, request):
        categories = ItemCategory.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response({'articles': serializer.data})

    def post(self, request):
        category = request.data.get('category')
        serializer = serializers.CategoryActionsSerializer(data=category)
        if serializer.is_valid():
            find_category = ItemCategory.objects.filter(name=category['name'])
            if len(find_category) != 0:
                return Response({'status': 'error',
                                'response': f'Category with name {category["name"]} already exists'},
                                status=HTTP_400_BAD_REQUEST)
            category_saved = serializer.save()
        else:
            return Response({'status': 'error',
                            'response': 'Incorrect data'},
                            status=HTTP_400_BAD_REQUEST)
        return Response({'status': 'success',
                        'response': f'Category \'{category["name"]}\' successfully created'},
                        status=HTTP_200_OK)

    def put(self, request):
        category = request.data.get('category')
        category_to_update = ItemCategory.objects.filter(name=category['name'])
        serializer = serializers.CategoryActionsSerializer(category_to_update, data=category)
        if serializer.is_valid():
            category_saved = serializer.save()
        else:
            return Response({'status': 'error',
                            'response': 'Incorrect data'},
                            status=HTTP_400_BAD_REQUEST)
        return Response({'status': 'success',
                        'response': f'Category \'{category["name"]}\' successfully updated'},
                        status=HTTP_200_OK)

    def delete(self, request):
        category = request.data.get('category')
        category_to_delete = ItemCategory.objects.filter(name=category['name'])
        if len(category_to_delete) == 0:
            return Response({'status': 'error',
                            'response': f'No category named \'{category["name"]}\'.'},
                            status=HTTP_404_NOT_FOUND)
        category_to_delete.delete()
        return Response({'status': 'success',
                        'response': f'Category \'{category["name"]}\' successfully deleted.'},
                        status=HTTP_200_OK)


class ItemChanges(generics.ListAPIView):
    '''Create, put and delete items'''

    def item_changes_creation(self, initial_quantity, item_in_db):
        item = Item.objects.get(pk=item_in_db.pk)
        ItemChange.objects.create(item=item,
                                initial_quantity=initial_quantity,
                                new_quantity=item_in_db.quantity)

    def post(self, request):
        item = request.data.get('item')
        serializer = serializers.ItemsSerializer(data=item)
        if serializer.is_valid():
            find_item = Item.objects.filter(name=item['name'])
            if len(find_item) != 0:
                return Response({'status': 'error',
                                'response': f'Item with name {item["name"]} already exists'},
                                status=HTTP_400_BAD_REQUEST)
            serializer.save()
        else:
            return Response({'status': 'error',
                            'response': 'Incorrect data'},
                            status=HTTP_400_BAD_REQUEST)
        item_in_db = Item.objects.get(name=item['name'])
        self.item_changes_creation(0, item_in_db)
        return Response({'status': 'success',
                        'response': f'Item \'{item["name"]}\' successfully created'},
                        status=HTTP_200_OK)

    def put(self, request):
        item = request.data.get('item')
        item_to_update = Item.objects.filter(name=item['name'])
        if len(item_to_update) != 0:
            initial_quantity = item_to_update[0].quantity
        serializer = serializers.ItemsSerializer(item_to_update, data=item)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'status': 'error',
                            'response': 'Incorrect data'},
                            status=HTTP_400_BAD_REQUEST)
        self.item_changes_creation(initial_quantity, item_to_update[0])
        return Response({'status': 'success',
                        'response': f'Item \'{item["name"]}\' successfully updated'},
                        status=HTTP_200_OK)

    def delete(self, request):
        item = request.data.get('item')
        item_to_delete = Item.objects.filter(name=item['name'])
        if len(item_to_delete) == 0:
            return Response({'status': 'error',
                            'response': f'No item named \'{item["name"]}\'.'},
                            status=HTTP_404_NOT_FOUND)
        item_to_delete.delete()
        return Response({'status': 'success',
                        'response': f'Item \'{item["name"]}\' successfully deleted.'},
                        status=HTTP_200_OK)
