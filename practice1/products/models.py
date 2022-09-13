from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField('Title', max_length=120)
    description = models.TextField('Description')
    price = models.DecimalField('Price', decimal_places=2, max_digits=1000)

    def __str__(self):
        return f"{self.__class__.__name__}<{self.id}, {self.title}>"

    def __repr__(self):
        return self.__str__()
    
    def get_absolute_url(self):
        return reverse("products:product_get_by_id", kwargs={"id": self.id})
