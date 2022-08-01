from enum import unique
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


def validate_title(value):
    queryset = Product.objects.filter(title__iexact=value)
    if queryset.exists():
        raise serializers.ValidationError(
            f"{value} is already a product name.")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())
