# Generated by Django 5.1.1 on 2024-09-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_remove_habit_tg_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='date',
            field=models.DateField(default='2024-09-16', verbose_name='дата привычки'),
        ),
    ]
