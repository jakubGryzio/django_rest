from asyncore import read
from cgitb import lookup
from pickletools import read_long1
from turtle import title
from requests import request
from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerilizer
from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerilizer(source='user', read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field="pk")
    title = serializers.CharField(
        validators=[validate_title_no_hello, unique_product_title])
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Product
        fields = [
            'owner',
            'email',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
            'public',
        ]

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     queryset = Product.objects.filter(title__iexact=value)
    #     if queryset.exists():
    #         raise serializers.ValidationError(
    #             f"{value} is already a product name.")
    #     return value

    """ def create(self, validated_data):
        # return Product.objects.create(**validated_data)
        # email = validated_data.pop('email')
        obj = super().create(validated_data)
        # print(email, obj)
        return obj """

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
