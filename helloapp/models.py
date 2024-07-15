from django.db import models

# Create your models here.

class Register(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    fullname = models.CharField(max_length = 100)
    address = models.CharField(max_length =100)
    def __str__(self):
        return self.email+ " " + self.password + " " + self.mobile + " " + self.fullname + " " + self.address     
