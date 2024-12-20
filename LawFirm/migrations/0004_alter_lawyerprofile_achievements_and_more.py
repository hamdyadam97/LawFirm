# Generated by Django 5.1.2 on 2024-10-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LawFirm', '0003_alter_lawyerprofile_practice_areas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyerprofile',
            name='achievements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lawyerprofile',
            name='education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lawyerprofile',
            name='years_of_experience',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
