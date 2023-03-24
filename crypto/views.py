import os

import json

import requests
from django.shortcuts import redirect, render

from .forms import WishListForm
from .models import Cryptocurrency, WishList

API_KEY_NEWS = os.getenv('API_KEY_NEWS')
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('X-CMC_PRO_API_KEY')
}


def index(request):
    return render(request, 'crypto/index.html')


def get_crypto(request):
    response = requests.get(url, headers=headers, params=parameters)
    data = json.loads(response.text)
    for currency in data['data']:
        Cryptocurrency.objects.update_or_create(
            id=currency['id'],
            # symbol=currency['symbol'],
            # name=currency['name'],
            # price=currency['quote']['USD']['price'],
            # volume=currency['quote']['USD']['volume_24h'],
            # percent_change=currency['quote']['USD']['percent_change_24h'],
            # market_cap=currency['quote']['USD']['market_cap'],
            defaults={
                'symbol': currency['symbol'],
                'name': currency['name'],
                'price': currency['quote']['USD']['price'],
                'volume': currency['quote']['USD']['volume_24h'],
                'percent_change': currency['quote']['USD']['percent_change_24h'],
                'market_cap': currency['quote']['USD']['market_cap']
            }
        )
    return render(request, 'crypto/results.html', {'crypto_list': Cryptocurrency.objects.all()})


def search_crypto(name):
    for crypto in Cryptocurrency.objects.all():
        if crypto.name.lower() == name or crypto.symbol.lower() == name:
            return crypto


def one_crypto_view(request):
    name = request.POST.get('name').lower()
    one_crypto = search_crypto(name=name)
    print(one_crypto)
    return render(request, 'crypto/one_crypto.html', {'one_crypto': one_crypto})


def add_wishlist(request):
    if request.method == 'POST':
        form = WishListForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('cryptopage:wishlist')
    else:
        form = WishListForm(user=request.user)
    return render(request, 'crypto/wishlist.html', {'form': form,
                                                    'wishlist': WishList.objects.filter(user=request.user.id)})


#Представление которое парсит и выводит 5 последних новостей по криптовалюте (опционально можно по определенной монете,
#это довольно просто реализовать(меняя 1 квери параметр))
def get_news(request):
    url = f'https://newsapi.org/v2/everything?q=cryptocurrency&from=2023-02-23&sortBy=publishedAt&apiKey={API_KEY_NEWS}'
    response = requests.get(url, params={'pageSize': 5})
    data = json.loads(response.text)
    news_list = []
    news = data['articles']
    for new in news:
        title = new['title']
        description = new['description']
        url = new['url']
        news_list.append([title, description, url])
    return render(request, 'crypto/news_paper.html', {'news': news_list})
