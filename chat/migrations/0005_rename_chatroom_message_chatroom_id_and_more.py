# Generated by Django 5.0.4 on 2024-04-17 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_chatroom_receiver_alter_chatroom_sender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='chatroom',
            new_name='chatroom_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='sender_id',
        ),
    ]
