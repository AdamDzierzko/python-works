from django.db import models

# Create your models here.

class Zadanie(models.Model):
    """Aktualne zadania do wykonania"""
    opis = models.TextField(max_length=499)
