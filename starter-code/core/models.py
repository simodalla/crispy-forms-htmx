from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Subjects(models.IntegerChoices):
        WEB_DEV = 1
        CYBER = 2
        DEVOPS = 3

    subject = models.PositiveSmallIntegerField(choices=Subjects.choices)
    date_of_birth = models.DateField()
