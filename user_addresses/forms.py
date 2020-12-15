from django import forms
from .models import UserAddresses


class UserAddressesForm(forms.ModelForm):
    class Meta:
        model = UserAddresses
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'additional_full_name': 'Full Name',
            'additional_phone_number': 'Phone Number',
            'additional_postcode': 'Postal Code',
            'additional_town_or_city': 'Town or City',
            'additional_street_address1': 'Street Address 1',
            'additional_street_address2': 'Street Address 2',
            'additional_county': 'County, State or Locality',
        }

        self.fields['additional_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'additional_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'  # noqa: 501
            self.fields[field].label = False
