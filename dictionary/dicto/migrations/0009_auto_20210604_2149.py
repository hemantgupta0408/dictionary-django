# Generated by Django 3.1.6 on 2021-06-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicto', '0008_auto_20210604_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='category',
            field=models.CharField(default='None', max_length=80),
        ),
    ]
