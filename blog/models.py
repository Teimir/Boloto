from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class New(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    bio = models.TextField(blank=True)


class Post(models.Model):
    title = models.CharField(max_length=100, default="", blank=True, null=True) #Не даёт нужного результата, всё ещё требует заголовок
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.FileField(upload_to='attachments/', blank=True)
