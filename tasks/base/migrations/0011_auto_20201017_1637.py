# Generated by Django 3.1.2 on 2020-10-17 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='Foods',
            new_name='foods',
        ),
    ]