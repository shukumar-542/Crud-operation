from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12,null=True)

    def __str__(self):
        return self.name