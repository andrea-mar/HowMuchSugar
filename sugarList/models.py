from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
        }


class Product(models.Model):
    productName = models.CharField(max_length=250)
    productBrand = models.CharField(max_length=250)
    productSugar = models.PositiveSmallIntegerField()
    productImage = models.ImageField(upload_to='img') # check document. on FileField
    dateAdded = models.DateTimeField(auto_now_add=True)

    def serialize(self): 
        return {
            'id': self.id,
            'productName': self.productName,
            'productBrand': self.productBrand,
            'productSugar': self.productSugar,
            'productImage': self.productImage,
            'dateAdded': self.dateAdded.strftime('%B %d, %Y, %I:%M %p'),
        }