from django import forms
from .models import Wallet


class WalletForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = ('wallet_pk', 'wallet_name')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'wallet_pk': 'Public Key',
            'wallet_name': 'Name your wallet',
        }

        self.fields['wallet_pk'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'  # noqa: 501
            self.fields[field].label = False
