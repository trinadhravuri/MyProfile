from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    message= models.TextField(max_length=1500)

    def __str__(self):
        return self.name