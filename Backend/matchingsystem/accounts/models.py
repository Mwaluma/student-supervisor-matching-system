from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Departments model
# class Departments(models.Model):
#     department_name= models.CharField(max_length= 100)
#     school= models.CharField(max_length= 300)
#
#         return self.department_name

# Lecturer model
class Lecturer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique= True)
    office_address= models.CharField(max_length=254)
    #department= models.ForeignKey('accounts.Departments', on_delete=models.CASCADE)

    def __str__(self):
        full_name= self.user.first_name + " " + self.user.last_name
        return full_name

    def get_lecturer_name(self):
        full_name= self.user.first_name + " " + self.user.last_name
        return self.full_name


class LecturerProfilePicture(models.Model):
    lecturer= models.OneToOneField('accounts.Lecturer', on_delete= models.CASCADE)
    picture= models.ImageField(upload_to= 'profile_pics/', blank= True)

    def __str__(self):
        return self.lecturer.user.username
