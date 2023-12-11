from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=50, widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        # password = cleaned_data.get("password")
        # password_repeat = cleaned_data.get("password_repeat")
        # if password_repeat != password:
        if cleaned_data.get("password") != cleaned_data.get("password_repeat"):
            raise forms.ValidationError("Password match!")
        
        cleaned_data.pop('password_repeat')
        
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)