from django.db import models


CHOICES = (('oil','Oil'),('grains','Grains'),('cosmetics','Cosmetics'),)
# Create your models here.
class Grocery(models.Model):
    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=100,choices=CHOICES)
    Quantity = models.IntegerField()
    RatePerUnit = models.IntegerField()
    Amount = models.IntegerField(null= True)


    def __str__(self):
        return self.Name + ' , ' + self.Type + ' , ' + str(self.Quantity) + ' , ' + str(self.RatePerUnit)

class TakeGrocery(models.Model):
    model = Grocery





    