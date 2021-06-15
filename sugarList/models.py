from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
        }


class Product(models.Model):
    productName = models.CharField(max_length=250, verbose_name='Name')
    productBrand = models.CharField(max_length=250, verbose_name='Brand')
    productSize = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Size(g)', default=0)
    productSugar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Sugar(per 100g)')
    productAddedSugar = models.BooleanField(verbose_name='Product has added sugar', default=False)
    productImage = models.ImageField(upload_to='img', verbose_name='Image') # check document. on FileField
    dateAdded = models.DateTimeField(auto_now_add=True)

    def serialize(self): 
        return {
            'id': self.id,
            'productName': self.productName,
            'productBrand': self.productBrand,
            'productSize': self.productSize,
            'productSugar': self.productSugar,
            'productAddedSugar': self.productAddedSugar,
            'productImage': self.productImage,
            'dateAdded': self.dateAdded.strftime('%B %d, %Y, %I:%M %p'),
        }