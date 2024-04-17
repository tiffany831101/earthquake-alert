# Generated by Django 5.0.4 on 2024-04-16 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chatroom_receiver_alter_chatroom_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='chat.user'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='chat.user'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to='chat.user'),
        ),
    ]