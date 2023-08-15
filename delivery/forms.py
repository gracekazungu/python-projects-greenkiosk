from django import forms
from.models import Delivery


# forms.py
class UploadDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__' 