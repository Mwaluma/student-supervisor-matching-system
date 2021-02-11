from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    doc= forms.FileField(label='Document')
    class Meta:
        model = Document
        fields = ['doc']
