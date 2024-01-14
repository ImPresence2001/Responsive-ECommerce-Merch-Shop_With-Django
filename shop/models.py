from django.db import models

# Create your models here.
class Featured_Product(models.Model):
    title = models.CharField(max_length=255)
    discount = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.title