# Generated by Django 5.1.4 on 2025-01-12 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.categoria'),
        ),
    ]
