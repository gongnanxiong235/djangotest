# Generated by Django 2.1.5 on 2019-01-15 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0002_auto_20190115_2230'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publish',
        ),
    ]