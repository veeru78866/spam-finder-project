from django.db import models

# Create your models here.

class RegisteredUsersModel(models.Model):
    username = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=10,unique=True)
    email = models.EmailField(default='xyz@abc.com')
    spam = models.BooleanField(default=False)

    def __str__(self):
        return self.username 

