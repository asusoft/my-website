# Generated by Django 4.0.1 on 2022-08-26 18:44

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_project_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('abstract', models.TextField()),
                ('picture', models.ImageField(default='me.jpg', upload_to='pics')),
                ('paper', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('repo', models.TextField(blank=True, default='#', validators=[django.core.validators.URLValidator()])),
                ('posted', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('topic', models.ManyToManyField(to='account.Topic')),
            ],
            options={
                'ordering': ['posted'],
            },
        ),
    ]
