# Generated by Django 3.1.6 on 2021-06-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicto', '0012_auto_20210606_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='category',
            field=models.CharField(blank=True, default=None, max_length=80),
        ),
    ]
