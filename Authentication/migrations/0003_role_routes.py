# Generated by Django 5.1.4 on 2025-01-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_alter_route_route_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='routes',
            field=models.JSONField(default=list),
        ),
    ]
