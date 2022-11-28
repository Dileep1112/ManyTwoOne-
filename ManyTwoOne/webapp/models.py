from django.db import models
# Create your models here.
class Team(models.Model):
    Tname=models.CharField(max_length=255)
    def __str__(self):
        return self.Tname
class Player(models.Model):
    Pname=models.CharField(max_length=255)
    Team=models.ForeignKey(Team,on_delete=models.CASCADE,)
    def __str__(self):
        return self.Pname