from django.db import models

class User(models.Model):
    email = models.EmailField
    username = models.CharField(max_length=None)

    firstname = models.CharField(max_length=None)
    middlename = models.CharField(max_length=None)
    lastname = models.CharField(max_length=None)

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    PREFER_NOT_TO_SAY = 'PNTS'
    GENDER_OPTIONS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (PREFER_NOT_TO_SAY, 'Prefer Not To Say'),
    ]
    gender = models.CharField('Gender', choices=GENDER_OPTIONS, default=PREFER_NOT_TO_SAY)

    age = models.IntegerField()
