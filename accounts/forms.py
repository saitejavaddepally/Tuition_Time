from django import forms
from .models import user_register

class user_register_form(forms.ModelForm):
    class Meta: 
        model = user_register
        fields = (
            "first_name",
            "last_name",
            "user_name",
            "email",
            "password"
        )