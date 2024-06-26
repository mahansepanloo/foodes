# Generated by Django 5.0.6 on 2024-06-01 16:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profileuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
