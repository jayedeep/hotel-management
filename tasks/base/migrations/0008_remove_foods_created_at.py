# Generated by Django 3.1.2 on 2020-10-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_foods_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foods',
            name='created_at',
        ),
    ]
