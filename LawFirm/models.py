# law_firms/models.py
from django.db import models
from User.models import User


class LawFirm(models.Model):
    class PracticeAreas(models.TextChoices):
        CIVIL_LAW = "CivilLaw", "Civil Law"
        CORPORATE_LAW = "CorporateLaw", "Corporate Law"
        CRIMINAL_LAW = "CriminalLaw", "Criminal Law"
        FAMILY_LAW = "FamilyLaw", "Family Law"
        TAX_LAW = "TaxLaw", "Tax Law"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='law_firm_profile')
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='law_firm_onwer',null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    logo = models.ImageField(upload_to='law_firms/logos/',blank=True,null=True)
    cover_image = models.ImageField(upload_to='law_firms/covers/',blank=True,null=True)
    founder_message = models.TextField(blank=True,null=True)
    services = models.TextField(blank=True,null=True)
    awards = models.TextField(blank=True,null=True)
    contact_email = models.EmailField(blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    social_media_links = models.JSONField(blank=True,null=True)  # You can store multiple links
    website_url = models.URLField(blank=True,null=True)
    # Related fields
    city = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    classification = models.CharField(max_length=50, choices=[
        ('local', 'محلي'),
        ('global', 'عالمي'),
    ],blank=True,null=True)
    practice_areas = models.CharField(blank=True, default=True,
                                      choices=PracticeAreas.choices,null=True)  # List of practice areas, e.g., civil, commercial, family, etc.

    def __str__(self):
        return self.user.username


class LawyerProfile(models.Model):
    class PracticeAreas(models.TextChoices):
        CIVIL_LAW = "CivilLaw", "Civil Law"
        CORPORATE_LAW = "CorporateLaw", "Corporate Law"
        CRIMINAL_LAW = "CriminalLaw", "Criminal Law"
        FAMILY_LAW = "FamilyLaw", "Family Law"
        TAX_LAW = "TaxLaw", "Tax Law"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lawyer_profile')
    license_number = models.CharField(max_length=100)
    law_firm = models.ForeignKey(LawFirm, on_delete=models.SET_NULL, null=True, blank=True)
    practice_areas = models.CharField(blank=True,null=True,choices=PracticeAreas.choices,)  # List of practice areas
    years_of_experience = models.PositiveIntegerField(null=True,blank=True)
    education = models.TextField(null=True,blank=True)
    achievements = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.display_name

