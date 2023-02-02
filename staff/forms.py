from django import forms

from cart.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'avaliable_colours', 'avaliable_sizes', 'primary_category', 'secondary_categories']