from rest_framework import serializers

from crypto.models import Cryptocurrency


class CryptocurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'

