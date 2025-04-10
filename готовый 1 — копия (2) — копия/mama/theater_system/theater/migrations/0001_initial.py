# Generated by Django 5.2 on 2025-04-03 19:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], default='M', max_length=1, verbose_name='Пол')),
                ('contact_info', models.TextField(verbose_name='Контактная информация')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], default='M', max_length=1, verbose_name='Пол')),
                ('contact_info', models.TextField(verbose_name='Контактная информация')),
                ('years_of_experience', models.IntegerField(default=0, verbose_name='Опыт работы (лет)')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название спектакля')),
                ('genre', models.CharField(max_length=100, verbose_name='Жанр')),
                ('duration', models.DurationField(verbose_name='Продолжительность')),
                ('description', models.TextField(verbose_name='Описание')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.director', verbose_name='Режиссер')),
            ],
            options={
                'verbose_name': 'Спектакль',
                'verbose_name_plural': 'Спектакли',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('location', models.CharField(max_length=200, verbose_name='Место представления')),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость билета')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.play', verbose_name='Спектакль')),
            ],
            options={
                'verbose_name': 'Представление',
                'verbose_name_plural': 'Представления',
            },
        ),
        migrations.CreateModel(
            name='Casting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('casting_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('P', 'В процессе'), ('A', 'Принят'), ('R', 'Отклонен')], default='P', max_length=1)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='castings', to='theater.actor')),
                ('play', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='castings', to='theater.play')),
            ],
            options={
                'verbose_name': 'Кастинг',
                'verbose_name_plural': 'Кастинги',
                'ordering': ['-casting_date'],
            },
        ),
        migrations.CreateModel(
            name='ActorRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100, verbose_name='Название роли')),
                ('role_info', models.TextField(verbose_name='Справочная информация')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.actor', verbose_name='Актер')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.play', verbose_name='Спектакль')),
            ],
            options={
                'verbose_name': 'Роль актера',
                'verbose_name_plural': 'Роли актеров',
            },
        ),
        migrations.AddField(
            model_name='actor',
            name='plays',
            field=models.ManyToManyField(through='theater.ActorRole', to='theater.play', verbose_name='Спектакли'),
        ),
    ]
