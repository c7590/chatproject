# Generated by Django 5.0.3 on 2024-03-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_userprofile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
