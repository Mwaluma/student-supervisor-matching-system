from django.db import models
from accounts.models import Lecturer

# Create your models here.
class Document(models.Model):
    author= models.ForeignKey(Lecturer, on_delete= models.CASCADE)
    doc= models.FileField(upload_to='documents/', max_length= 1000)

    def __str__(self):
        return self.author.user.first_name  + " " + self.author.user.last_name
