from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    message = models.TextField()