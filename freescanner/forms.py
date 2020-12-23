from django import forms
from .models import Identifiers


class FreescannerForm(forms.ModelForm):

    class Meta:
        model = Identifiers
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'identifier_id': 'Identifier, e.g. contract or address',
            'identifier_name': 'Name the identifier, e.g. Bittorrent Staking',
            'identifier_type': 'Select type of identifier',
            'identifier_comment': 'Describe the Identifier, max 250 digits',
        }

        self.fields['identifier_id'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'  # noqa: 501
            self.fields[field].label = False
