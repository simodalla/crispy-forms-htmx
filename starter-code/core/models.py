from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Subjects(models.IntegerChoices):
        WEB_DEVELOPMENT = 1
        SYSTEMS_PROGRAMMING = 2
        DATA_SCIENCES = 3

    subject = models.PositiveSmallIntegerField(choices=Subjects.choices)
    date_of_birth = models.DateField()
