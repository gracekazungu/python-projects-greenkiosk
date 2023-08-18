from django import forms
from.models import Cart


# forms.py
class UploadCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'  


