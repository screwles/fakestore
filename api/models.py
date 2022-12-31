from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    image=models.ImageField(null=True,upload_to="images")
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=200)


    def __str__(self):
        return self.name
    


class Reviews(models.Model):
    Product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])



class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed", "order-placed"),
        ("removed","removed")
    )
    status=models.CharField(max_length=120,choices=options,default="in-cart")