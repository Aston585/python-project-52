from django.contrib.auth.views import get_user_model
from django import forms


class UserCreate(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'
