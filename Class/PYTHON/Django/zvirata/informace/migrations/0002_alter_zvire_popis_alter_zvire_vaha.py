# Generated by Django 4.0.3 on 2022-04-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zvire',
            name='popis',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='zvire',
            name='vaha',
            field=models.IntegerField(null=True),
        ),
    ]
