# Generated by Django 2.2.2 on 2019-06-27 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
                ('email', models.EmailField(max_length=20, verbose_name='Email')),
                ('sent_to', models.DateField(auto_now_add=True, verbose_name='Отправленно')),
                ('sent_email', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Собщения',
                'verbose_name_plural': 'Собщение',
                'ordering': ['-sent_to'],
            },
        ),
    ]
