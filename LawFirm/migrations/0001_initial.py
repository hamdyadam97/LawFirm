# Generated by Django 5.1.1 on 2024-10-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LawFirm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='law_firms/logos/')),
                ('cover_image', models.ImageField(upload_to='law_firms/covers/')),
                ('founder_message', models.TextField()),
                ('services', models.TextField()),
                ('awards', models.TextField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('social_media_links', models.JSONField()),
                ('website_url', models.URLField()),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('classification', models.CharField(choices=[('local', 'محلي'), ('global', 'عالمي')], max_length=50)),
                ('practice_areas', models.JSONField()),
            ],
        ),
    ]
