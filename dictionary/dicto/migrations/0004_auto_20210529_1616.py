# Generated by Django 3.1.6 on 2021-05-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicto', '0003_auto_20210529_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='eword',
            field=models.CharField(max_length=30),
        ),
    ]
