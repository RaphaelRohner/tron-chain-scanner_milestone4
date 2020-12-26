from django import forms
from .models import Identifiers


# class FreescannerForm(forms.ModelForm):


class IdentifiersForm(forms.ModelForm):

    class Meta:
        model = Identifiers
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'identifier_contract': 'Identifier, e.g. contract or address',
            'identifier_name': 'Name the identifier, e.g. Bittorrent Staking',
            'identifier_comment': 'Describe the Identifier, max 250 digits',
        }

        self.fields['identifier_contract'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'  # noqa: 501
            self.fields[field].label = False
            if field != 'identifier_type':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
