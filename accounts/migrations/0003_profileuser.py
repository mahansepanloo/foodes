# Generated by Django 5.0.6 on 2024-06-01 15:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_optcode_alter_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=100, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]