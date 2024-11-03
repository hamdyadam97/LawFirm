# Generated by Django 5.1.2 on 2024-10-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LawFirm', '0007_alter_lawfirm_awards_alter_lawfirm_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawfirm',
            name='practice_areas',
            field=models.CharField(blank=True, choices=[('CivilLaw', 'Civil Law'), ('CorporateLaw', 'Corporate Law'), ('CriminalLaw', 'Criminal Law'), ('FamilyLaw', 'Family Law'), ('TaxLaw', 'Tax Law')], default=True, null=True),
        ),
        migrations.AlterField(
            model_name='lawyerprofile',
            name='practice_areas',
            field=models.CharField(blank=True, choices=[('CivilLaw', 'Civil Law'), ('CorporateLaw', 'Corporate Law'), ('CriminalLaw', 'Criminal Law'), ('FamilyLaw', 'Family Law'), ('TaxLaw', 'Tax Law')], null=True),
        ),
    ]
