from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
 


