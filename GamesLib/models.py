from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
