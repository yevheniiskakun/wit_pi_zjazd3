from django.db import models
from rest_framework import serializers

class Product(models.Model):
    name = models.CharField(blank=False, max_length=255)
    buyed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'buyed']