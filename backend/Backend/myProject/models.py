from django.db import models

class Employee(models.Model):
    firstname =models.CharField('First Name',max_length=255)
    lastname =models.CharField('Last Name',max_length=255)
 


