# Generated by Django 5.0.6 on 2024-06-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profileuser_age_alter_profileuser_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='age',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='bio',
            field=models.TextField(blank=True, default='  ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='firstname',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='lastname',
            field=models.CharField(blank=True, default='  ', max_length=100, null=True),
        ),
    ]
