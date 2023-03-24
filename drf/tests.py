import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from crypto.models import Cryptocurrency
from drf.serializers import CryptocurrencySerializers

client = APIClient()


@pytest.mark.django_db
def test_cryptocurrency_list_api():
    # Создадим объекты бд для проверки
    cryptocurrency1 = Cryptocurrency.objects.create(id=99998, name="Bitcoin", symbol="BTC")
    cryptocurrency2 = Cryptocurrency.objects.create(id=99999, name="Ethereum", symbol="ETH")

    # Получаем этот список
    url = reverse('apipage:list')
    response = client.get(url)
    cryptocurrency_data = Cryptocurrency.objects.all()
    serializer = CryptocurrencySerializers(cryptocurrency_data, many=True)

    # Проверяем ответ
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data


@pytest.mark.django_db
def test_cryptocurrency_create_api():
    # Вводим данные для создания объекта бд
    data = {'id': 99999, 'name': 'Bitcoin', 'symbol': 'BTC'}
    url = reverse('apipage:list')

    # Отправляем пост запрос
    response = client.post(url, data=data, format='json')

    # Проверяем ответ
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_cryptocurrency_retrieve_api():
    # Создадим объекты бд для проверки
    cryptocurrency = Cryptocurrency.objects.create(id=99999, name="Bitcoin", symbol="BTC")

    # Отправляем гет запрос
    url = reverse('apipage:one', args=[cryptocurrency.symbol])
    response = client.get(url)

    # Проверяем ответ
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == cryptocurrency.name
    assert response.data['symbol'] == cryptocurrency.symbol


@pytest.mark.django_db
def test_cryptocurrency_update_api():
    # Создадим объекты бд для проверки
    cryptocurrency = Cryptocurrency.objects.create(id=99999, name="Bitcoin", symbol="BTC")
    data = {'id': 99999, 'name': 'Ethereum', 'symbol': 'ETH'}

    # Отправляем пут запрос для обновления записи
    url = reverse('apipage:one', args=[cryptocurrency.symbol])
    response = client.put(url, data=data, format='json')

    # Проверяем ответ
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Ethereum'
    assert response.data['symbol'] == 'ETH'


@pytest.mark.django_db
def test_cryptocurrency_delete_api():
    # Создадим объекты бд для проверки
    cryptocurrency = Cryptocurrency.objects.create(id=99999, name="Bitcoin", symbol="BTC")

    # Отправляем делит запрос для удаление из бд
    url = reverse('apipage:one', args=[cryptocurrency.symbol])
    response = client.delete(url)

    # Проверяем ответ
    assert response.status_code == status.HTTP_204_NO_CONTENT


