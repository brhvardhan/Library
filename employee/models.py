from django.db import models

# Create your models here.
class Books(models.Model):
    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Total_quantity = models.IntegerField()
    Stock_quantity = models.IntegerField()
    def __str__(self):
        return self.Name