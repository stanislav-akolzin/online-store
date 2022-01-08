from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.core.validators import MinLengthValidator, MinValueValidator


class ItemCategory(models.Model):
    '''The category of item'''
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name

    def count_items(self):
        return self.item_set.count()


class Item(models.Model):
    '''Items in online shop'''
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural = 'items'

    def __str__(self) -> str:
        return self.name

    def item_changes(self):
        changes = ItemChange.objects.filter(item=self.id)
        changes_list = []
        for change in changes:
            changes_dict = {}
            changes_dict['date'] = change.date
            changes_dict['initial_quantity'] = change.initial_quantity
            changes_dict['new_quantity'] = change.new_quantity
            changes_list.append(changes_dict)
        return changes_list



class ItemChange(models.Model):
    '''All items quantity changes'''
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    initial_quantity = models.IntegerField()
    new_quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'quantity changes'

    def __str__(self) -> str:
        return self.item.name + ' ' + str(self.date)