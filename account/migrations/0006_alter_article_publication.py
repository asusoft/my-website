# Generated by Django 4.0.1 on 2022-08-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_reference_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication',
            field=models.ManyToManyField(blank=True, to='account.Publication'),
        ),
    ]
