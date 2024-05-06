from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/')


PHONE_TYPE = (
    ('Primary' , 'Primary') ,
    ('Secondry' , 'Secondry') ,
)


class Phones(models.Model):
    user = models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE)
    type = models.CharField(max_length=20,choices=PHONE_TYPE)
    number = models.CharField(max_length=25)

    def __str__(self):
        return str(self.user)


ADDRESS_TYPE = (
    ('Home' , 'Home') ,
    ('office' , 'Office') ,
    ('Bussines' , 'Bussines',) ,
    ('Other' , 'Other') ,
)


class Address(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    address = models.TextField(max_length=300)
    type = models.CharField(max_length=20,choices=ADDRESS_TYPE)

    def __str__(self):
        return self.address
