from django import forms

from uploads.core.models import Doc


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ('description', 'document' )
