# Generated by Django 5.1.3 on 2024-11-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='users', to='core.role'),
        ),
    ]
