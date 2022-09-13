from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    # Override the default view
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Product Title"}))
    # description = forms.CharField(required=False, label='Description', widget=forms.TextInput(attrs={"placeholder": "Product Description"}))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={"placeholder": "Product Description"}))
    price = forms.DecimalField(initial=0.0)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'Product' in title:
            raise forms.ValidationError("Not a valid title")
        return title
