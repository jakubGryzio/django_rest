import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by('?').first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = serializer.data
        return Response(data)
    return Response({"invalid": "invalid data"}, status=400)