# Generated by Django 3.0.2 on 2020-01-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_reserve_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional',
            name='child_num',
            field=models.CharField(max_length=10),
        ),
    ]