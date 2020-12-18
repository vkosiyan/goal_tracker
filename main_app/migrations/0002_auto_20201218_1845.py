# Generated by Django 3.1.4 on 2020-12-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='category',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goaldate',
            field=models.DateField(blank=True, null=True, verbose_name='set goal date'),
        ),
    ]
