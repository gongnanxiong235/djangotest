# Generated by Django 2.1.5 on 2019-01-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.AlterModelOptions(
            name='publish',
            options={},
        ),
    ]