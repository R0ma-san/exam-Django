from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User 


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE,)

    

    def __str__(self):
        return self.title