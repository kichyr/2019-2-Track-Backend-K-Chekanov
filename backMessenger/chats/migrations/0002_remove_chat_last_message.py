# Generated by Django 2.2.5 on 2019-11-13 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='last_message',
        ),
    ]