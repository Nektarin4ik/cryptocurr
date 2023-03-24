from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from crypto.models import Cryptocurrency

from .serializers import CryptocurrencySerializers

# Create your views here.


# Если будет необходима пагинация
class ProductPaginator(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CryptocurrencyList(generics.ListCreateAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializers


class CryptocurrencyRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializers
    lookup_field = 'symbol'

