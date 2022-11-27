from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20)
    wrong = models.IntegerField(default=0)
    seconds = models.DecimalField(max_digits = 7,decimal_places=3, default=0)
    launcher = models.BooleanField(default=False)
    winner = models.BooleanField(default=False)
    
class Status(models.Model):
    status = models.CharField(max_length=5)
