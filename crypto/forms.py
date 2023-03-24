from django import forms

from .models import Cryptocurrency, WishList


class WishListForm(forms.Form):
    cryptocurrency = forms.ModelChoiceField(queryset=Cryptocurrency.objects.all())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self):
        wishlist = WishList.objects.create(
            user=self.user,
            cryptocurrency=self.cleaned_data['cryptocurrency']
        )
        return wishlist
