from django.db import models

# Create your models here.

GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
]


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER)
    image_file = models.ImageField(upload_to='images', null=True, verbose_name="")
    prediction_result = models.BooleanField(default=False)


    def __str__(self):
        return self.image_name +  ":" + str(self.image_file)