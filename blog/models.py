from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    bio = models.TextField(blank=True)


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    parent_post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='child_comments', null=True,
                                    blank=True)
    #title = models.CharField(max_length=100, default="", blank=True, null=True) #Не даёт нужного результата, всё ещё требует заголовок
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.FileField(upload_to='attachments/', blank=True)
