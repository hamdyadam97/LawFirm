# Generated by Django 5.1.1 on 2024-10-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_user_type_customerprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
