from django import forms
from app1.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        labels={'username':'Username ','email':'Email ','password':'Password ',}
        help_texts={'username':''}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['adress','profile_pic']
        labels={'adress':'adress ','profile_pic':'profile-pic ',}
        widgets={'adress':forms.Textarea(attrs={'cols':21,'rows':2})}
