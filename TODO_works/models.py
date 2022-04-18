from django.db import models


class Task(models.Model):
    """Tasks to do"""
    opis = models.TextField(max_length=499, blank=False)
