from django.db import models
from django.db.models import Model

# Create your models here.

class Product(Model):
    CURRENCY_CHOICES = (
        ('USD', 'US Dollars'),
        ('PES', 'Pesos'),
        ('REA', 'Reales'),
        ('EUR', 'Euros'),
    )

    WAREHOUSE_CHOICES = (
        ('CL', 'Chile'),
        ('AR', 'Argentina'),
        ('CN', 'China'),
        ('PE', 'Peru'),
        ('PA', 'Panama'),
        ('CO', 'Colombia'),
    )

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    warehouse = models.CharField(max_length=2,choices=WAREHOUSE_CHOICES)
    code = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    expiration_date = models.DateField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.name

class Image(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')