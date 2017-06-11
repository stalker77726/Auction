from django import forms
from django.contrib.auth.models import User
from .models import Lot_sub
from .models import UserProfile

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = 'Enter the ' + field_name   

class UserForm(BaseForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(BaseForm):
    class Meta:
        model = UserProfile
        fields = ()

class LotForm(BaseForm):
        class Meta:
            model = Lot_sub
            fields = ('title', 'text',)