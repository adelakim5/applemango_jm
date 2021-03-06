# Generated by Django 3.0.2 on 2020-01-14 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello', '0004_auto_20200114_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('parent', models.CharField(blank=True, max_length=2, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('sibling', models.CharField(blank=True, max_length=10, null=True)),
                ('marriage', models.CharField(blank=True, max_length=3, null=True)),
                ('child', models.CharField(blank=True, max_length=3, null=True)),
                ('child_num', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
