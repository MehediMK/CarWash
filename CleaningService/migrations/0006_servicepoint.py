# Generated by Django 3.2.7 on 2021-09-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CleaningService', '0005_auto_20210927_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SPName', models.CharField(max_length=100, verbose_name='Shop Name')),
                ('SPAddress', models.CharField(max_length=200)),
                ('SPPhone', models.CharField(blank=True, max_length=16)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
