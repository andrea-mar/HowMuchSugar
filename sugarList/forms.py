from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'productName',  
            'productBrand',
            'productSize',
            'productSugar', 
            'productAddedSugar',
            'productImage'
        )

    
