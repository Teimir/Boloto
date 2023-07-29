from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class New(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Newa(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    data = models.DateTimeField(default=timezone.now)