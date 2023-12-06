from django import forms
from post.models import Product

class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    rate = forms.IntegerField(min_value=1, max_value=5)

class CetagoryCreateForm(forms.Form):
    categoty_name = forms.CharField(max_length=100)
    price_range = forms.IntegerField(min_value=1, max_value=1000)
    brand = forms.CharField(max_length=100)


class ReviewCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    rate = forms.IntegerField(min_value=1, max_value=5)
    
    review = forms.CharField(widget=forms.Textarea())