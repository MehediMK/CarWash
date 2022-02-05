# Generated by Django 3.2.7 on 2021-09-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CleaningService', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleaningPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPName', models.CharField(max_length=100)),
                ('CPPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('CPItems', models.ManyToManyField(to='CleaningService.CleanningService')),
            ],
        ),
    ]