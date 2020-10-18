# Generated by Django 3.1.2 on 2020-10-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_invoice_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='restaurant',
            new_name='restaurants',
        ),
        migrations.AddField(
            model_name='invoice',
            name='table_no',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]