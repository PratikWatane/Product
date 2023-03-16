from  django import forms

from .models import Login


class Login_page(forms.ModelForm):

    class Meta:
        model = Login
        fields = "__all__"