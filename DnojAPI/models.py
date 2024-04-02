from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()
    description = models.TextField(default="")
                                   
    
    
    