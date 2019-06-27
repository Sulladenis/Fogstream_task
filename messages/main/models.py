from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .utilities import post_save_dispacher

class Message(models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст')
    email = models.EmailField(max_length=20, verbose_name='Email')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Отправитель')
    sent_to = models.DateField(auto_now_add=True, verbose_name='Отправленно')
    sent_email = models.BooleanField(default=False)

    def __str__(self):
        return 'message from {} sent: {}'.format(self.user, self.sent_to)

    class Meta:
        verbose_name_plural = 'Собщение'
        verbose_name = 'Собщения'
        ordering = ['-sent_to']


post_save.connect(post_save_dispacher, sender=Message)