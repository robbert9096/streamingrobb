from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SingUpForm(UserCreationForm):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "type":"text",
            "class":"form-control mb-0",
            "id":"username",
            "placeholder":"Enter Username",
            "required" : ""
        })

        self.fields['email'].widget.attrs.update({
            "type":"text",
            "class":"form-control mb-0",
            "id":"email",
            "placeholder":"Enter Email",
            "required" : ""
        })

        self.fields['password1'].widget.attrs.update({
            "type":"text",
            "class":"form-control mb-0",
            "id":"password1",
            "placeholder":"Enter Password",
            "required" : ""
        })

        self.fields['password2'].widget.attrs.update({
            "type":"text",
            "class":"form-control mb-0",
            "id":"password2",
            "placeholder":"Confirm Password",
            "required" : ""
        })
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
            

class UserUpdateForm(forms.ModelForm):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            "type":"text",
            "class":"form-control mb-0",
            "id":"first_name",
            "placeholder":"Enter First Name",
            "required" : ""
        })

        self.fields['last_name'].widget.attrs.update({
            "type":"text",
            "class":"form-control mb-0",
            "id":"last_name",
            "placeholder":"Enter Last Name",
            "required" : ""
        })
    
    class Meta:
        first_name = forms.CharField(max_length=50)
        last_name = forms.CharField(max_length=50)
        model = User
        fields = [ "first_name", "last_name"]

