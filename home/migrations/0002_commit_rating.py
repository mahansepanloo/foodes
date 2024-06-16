# Generated by Django 5.0.6 on 2024-06-16 15:17

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('is_reply', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fcomments', to='home.food')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rcomments', to='home.commit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ucomment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frate', to='home.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]