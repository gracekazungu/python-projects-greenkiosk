from django import forms
from.models import Cart


# forms.py
class UploadProductForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'  # Adjust fields as needed
