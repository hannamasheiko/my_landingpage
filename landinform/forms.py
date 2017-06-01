from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["full_name","email"]

    def clean_email(self):
        email =  (self.cleaned_data.get('email'))
        email_base, provider = email.split("@")
        domain, extention = provider.split(".")
        #if not extention == "edu" :
         #   raise forms.ValidationError("Plese use a valid .EDU email address")
        return email

    def cleaned_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name