from django.urls import path

from .views import add_wishlist, get_crypto, get_news, index, one_crypto_view

app_name = 'cryptopage'

urlpatterns = [
    path('', index, name='index'),
    path('all_crypto', get_crypto, name='all'),
    path('one_crypto', one_crypto_view, name='one'),
    path('wishlist', add_wishlist, name='wishlist'),
    path('news', get_news, name='news'),
                ]