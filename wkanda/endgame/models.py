from django.db import models

# Create your models here.


class Avengers(models.Model):
    name = models.CharField(max_length=20)
    weapon = models.CharField(max_length=10)
    avatar = models.CharField(max_length=3000)
    is_capable_to_take_mjollnir = models.BooleanField()


