# Generated by Django 5.0.4 on 2024-04-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_rename_chatroom_message_chatroom_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
