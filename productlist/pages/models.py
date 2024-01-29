from django.db import models
from rest_framework import serializers

class Product(models.Model):
    name = models.CharField(blank=False, max_length=255)
    buyed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'buyed']

    name = serializers.CharField(max_length=255, read_only=False)
    buyed = serializers.BooleanField(read_only=False)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        buyed = validated_data.get("buyed")

        instance.buyed = validated_data.get("buyed", instance.buyed)
        instance.save()

        return instance