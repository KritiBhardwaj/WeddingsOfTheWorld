# Generated by Django 3.0.8 on 2020-10-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200922_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='amount',
        ),
        migrations.AddField(
            model_name='pledge',
            name='image',
            field=models.URLField(default='https://via.placeholder.com/300.jpg'),
        ),
    ]