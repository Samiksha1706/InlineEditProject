from django.db import models

# Create your models here.

class Product(models.Model):
    PR_NAME = models.CharField(max_length=250)
    PR_PRICE = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    PR_AVAILABLE = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'product'
