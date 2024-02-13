# Generated by Django 5.0.2 on 2024-02-13 17:24

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок поста', max_length=128, validators=[django.core.validators.MinLengthValidator(limit_value=2)], verbose_name='заголовок')),
                ('body', models.TextField(help_text='Тест поста', verbose_name='текст')),
                ('slug', models.SlugField(help_text='URL', max_length=128, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=2)], verbose_name='URL')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('is_published', models.BooleanField(db_index=True, default=False, help_text='Опубликован', verbose_name='опубликован')),
                ('category', models.ForeignKey(help_text='Категория поста', on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': ('пост',),
                'verbose_name_plural': 'посты',
                'ordering': ['category', 'date_created'],
            },
        ),
    ]