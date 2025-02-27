
from django.db import models
from django.contrib.auth.models import User


class Archive(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.title
