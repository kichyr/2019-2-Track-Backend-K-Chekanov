from django.db import models
from chats.models import Chat, Message
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField('Email адрес', unique=True, null=True)
    first_name = models.CharField('Имя', max_length=30, blank=True, null=True)
    last_name = models.CharField(
        'Фамилия',
        max_length=30,
        blank=True,
        null=True)
    avatar = models.ImageField(
        'Аватар',
        upload_to='avatars/',
        null=True,
        blank=True)
    login = models.CharField(
        'Логин',
        max_length=10,
        unique=True,
        null=True,
        blank=False)

    """ def save(self, *args, **kwargs):
        self.username = self.login
        super.save(*args, **kwargs) """

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Member(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        verbose_name='Чат')
    last_read_message = models.ForeignKey(
        Message,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Последнее прочитанное сообщение'
    )

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class Attachment(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name='Сообщение')
    url = models.CharField('URL', max_length=40, null=True)

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
