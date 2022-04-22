# Generated by Django 3.2.10 on 2022-04-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]