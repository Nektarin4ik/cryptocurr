from django.urls import path

from .views import CryptocurrencyList, CryptocurrencyRUD

app_name = 'apipage'

urlpatterns = [
    path('v1/cryptocurrencylist', CryptocurrencyList.as_view(), name='list'),
    path('v1/cryptocurrencylist/<str:symbol>', CryptocurrencyRUD.as_view(), name='one')
]