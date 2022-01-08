'''URLs for Store app'''
from django.urls import path
from . import views


app_name = 'store'
urlpatterns = [
    path('items/', views.ItemList.as_view()),
    path('items/<int:pk>/', views.ItemDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('items/change/', views.ItemChanges.as_view()),
]