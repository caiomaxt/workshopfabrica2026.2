from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Usuario(AbstractUser):
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        null=True, 
        blank=True
    )
    phone = models.CharField(max_length=15, blank=True)