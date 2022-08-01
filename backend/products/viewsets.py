from itertools import product
from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # default



class ProductGenericViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # default

""" product_list = ProductGenericViewSet.as_view({'get': 'list'})
product_detail_list = ProductGenericViewSet.as_view({
    'get': 'retrive'
}) """
