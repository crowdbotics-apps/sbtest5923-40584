# Generated by Django 2.2.28 on 2023-05-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_m1'),
    ]

    operations = [
        migrations.AddField(
            model_name='m1',
            name='data1',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='m1',
            name='int1',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='m1',
            name='time1',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
