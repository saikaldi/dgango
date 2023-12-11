from django import forms
from post.models import Product

class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    rate = forms.IntegerField(min_value=1, max_value=5)
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title)<10:
            raise forms.ValidationError('Title to short')
        return title

class CetagoryCreateForm(forms.Form):
    categoty_name = forms.CharField(max_length=100)
    price_range = forms.IntegerField(min_value=1, max_value=1000)
    brand = forms.CharField(max_length=100)


class ReviewCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    rate = forms.IntegerField(min_value=1, max_value=5)
    review = forms.CharField(widget=forms.Textarea())

    # def clean(self):
    #     cleaned_data = super().clean()
    #     pass