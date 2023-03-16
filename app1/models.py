from django.db import models

# Create your models here.
  

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


    class Meta:
        db_table = "login"