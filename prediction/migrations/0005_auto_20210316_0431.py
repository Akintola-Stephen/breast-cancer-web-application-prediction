# Generated by Django 3.0.1 on 2021-03-16 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_auto_20210316_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(default='1998-07-04'),
        ),
    ]
