from django.db import models

# Create your models here.

GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
]


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)
    dob = models.DateField(default="1997-07-04")
    image_file = models.ImageField(
        upload_to='media/', null=True, verbose_name="")
    note = models.CharField(max_length=100)
    prediction_result = models.BooleanField(default=False)
