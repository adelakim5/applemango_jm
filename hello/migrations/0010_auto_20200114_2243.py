# Generated by Django 3.0.2 on 2020-01-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20200114_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional',
            name='child_num',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
    ]
