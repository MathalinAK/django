# Generated by Django 4.2.15 on 2024-10-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dproj1', '0005_persondetails_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetails',
            name='username',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
