from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    call_us = models.CharField(max_length=30)
    email_us = models.EmailField()
    subtitle = models.TextField(max_length=200)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    emails = models.TextField(max_length=100)
    phones = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    mobile_app = models.TextField(max_length=300,null=True, blank=True)
    android_url = models.URLField(null=True, blank=True)
    iphone_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
