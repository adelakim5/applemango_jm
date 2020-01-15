# Generated by Django 2.2.6 on 2020-01-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_auto_20200114_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='additional',
            name='school',
            field=models.CharField(blank=True, choices=[('elementary', '초등학교 졸업'), ('middle', '중학교 졸업'), ('high', '고등학교 졸업'), ('college', '대학교(2년제)졸업'), ('university', '대학교(4년제)졸업'), ('graduate', '대학원 졸업 이상'), ('others', '기타')], default='elementary', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='additional',
            name='school_others',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
