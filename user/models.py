from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class User (AbstractUser):
    age_min = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(120)], default=15)
    can_be_contacted = models.BooleanField(null=False)
    data_can_be_shared = models.BooleanField(null=False)

    def __str__(self):
        return self.username
