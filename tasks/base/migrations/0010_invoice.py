# Generated by Django 3.1.2 on 2020-10-17 10:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_foods_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Foods', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('totalbill', models.CharField(max_length=100)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.restaurants')),
            ],
        ),
    ]
