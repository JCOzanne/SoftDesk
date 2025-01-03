from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User (AbstractUser):

    """
     A custom user model extending Django's AbstractUser.
    Attributes:
        age_min (PositiveIntegerField): The minimum age of the user (for GDPR compliance).
        can_be_contacted (BooleanField): Whether the user consents to being contacted.
        data_can_be_shared (BooleanField): Whether the user consents to sharing their
    """

    age_min = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(120)], default=15)
    can_be_contacted = models.BooleanField(null=False)
    data_can_be_shared = models.BooleanField(null=False)

    def __str__(self):
        return self.username
