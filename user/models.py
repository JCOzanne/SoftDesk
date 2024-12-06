from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class User (AbstractUser):
    age_min = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(120)])
    can_be_contacted = models.BooleanField()
    data_can_be_shared = models.BooleanField()
