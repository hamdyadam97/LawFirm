# Generated by Django 5.1.2 on 2024-11-03 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_user_owner_of_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='owner_of_company',
        ),
    ]