# Generated by Django 4.0.1 on 2022-08-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_topic_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='picture',
            field=models.ImageField(default='me.jpg', upload_to='pics'),
        ),
    ]
