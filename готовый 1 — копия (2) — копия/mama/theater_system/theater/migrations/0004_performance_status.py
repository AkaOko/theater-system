# Generated by Django 5.2 on 2025-04-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0003_performance_actors_performance_ticket_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Запланировано'), ('in_progress', 'В процессе'), ('completed', 'Завершено')], default='scheduled', max_length=20, verbose_name='Статус'),
        ),
    ]
