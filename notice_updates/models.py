from django.db import models

# Create your models here
class subscription(models.Model):
    emails = models.EmailField('Email:', max_length=250)
    category = models.CharField('Category:', max_length=250)