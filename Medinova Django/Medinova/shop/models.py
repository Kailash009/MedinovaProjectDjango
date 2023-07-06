from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.BigIntegerField()
    pimage=models.ImageField(null=True,blank=True)
    pdesc=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name
    




