from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Cryptocurrency(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)
    volume = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)
    percent_change = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)
    market_cap = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.cryptocurrency.name}"


# Вариант с возможностью сохранять историю изменений цены, объемов и т.д
# class CryptoInfo(models.Model):
#     symbol = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE, to_field='symbol', null=True)
#     price = models.DecimalField(max_digits=8, decimal_places=6)
#     volume = models.DecimalField(max_digits=12, decimal_places=6)
#     percent_change = models.DecimalField(max_digits=12, decimal_places=6)
#     market_cap = models.DecimalField(max_digits=30, decimal_places=6)
#     get_time = models.DateTimeField(auto_now_add=True)