from django.db import models
#from django.conf import model
#from django.utils import TIME_ZONE

# Create your models here.

class createUser(models.Model):
    UserName=models.TextField()
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
    
    def publish(self):
        self.save()