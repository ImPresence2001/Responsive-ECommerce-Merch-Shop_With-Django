from django.db import models

# Create your models here.
class Featured_Product(models.Model):
    title = models.CharField(max_length=255)
    discount = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/featured')

    def __str__(self):
        return self.title