
from django.db import models

# Create your models here.
class Member(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
