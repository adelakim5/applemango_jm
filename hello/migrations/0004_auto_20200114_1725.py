# Generated by Django 3.0.2 on 2020-01-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20200114_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='emotion',
            field=models.CharField(choices=[('기쁨', '기쁨'), ('혐오', '혐오'), ('두려움', '두려움'), ('분노', '분노'), ('슬픔', '슬픔'), ('기타', '기타')], default='기쁨', max_length=3),
        ),
        migrations.AddField(
            model_name='diary',
            name='other',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
