from django.db import models

# Create your models here.


class Chat(models.Model):
    is_group_chat = models.BooleanField('Груповой Чат')
    topic = models.CharField('Топик', max_length=30)
    last_message = models.TextField('Текст последнего сообщения', null=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    content = models.TextField('Текст сообщения')
    added_at = models.DateTimeField('Дата отправки', blank=False, null=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    users = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        null=True
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['added_at']
