# law_firms/models.py
from django.db import models
from User.models import User


class LawFirm(models.Model):
    class PracticeAreas(models.TextChoices):
        CIVIL_LAW = "Civil Law", "Civil Law"
        CORPORATE_LAW = "Corporate Law", "Corporate Law"
        CRIMINAL_LAW = "Criminal Law", "Criminal Law"
        FAMILY_LAW = "Family Law", "Family Law"
        TAX_LAW = "Tax Law", "Tax Law"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='law_firm_profile')
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='law_firms/logos/')
    cover_image = models.ImageField(upload_to='law_firms/covers/')
    founder_message = models.TextField()
    services = models.TextField()
    awards = models.TextField()
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    social_media_links = models.JSONField()  # You can store multiple links
    website_url = models.URLField()

    # Related fields
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    classification = models.CharField(max_length=50, choices=[
        ('local', 'محلي'),
        ('global', 'عالمي'),
    ])
    practice_areas = models.CharField(blank=True, default=True,
                                      choices=PracticeAreas.choices)  # List of practice areas, e.g., civil, commercial, family, etc.

    def __str__(self):
        return self.name


class LawyerProfile(models.Model):
    class PracticeAreas(models.TextChoices):
        CIVIL_LAW = "Civil Law", "Civil Law"
        CORPORATE_LAW = "Corporate Law", "Corporate Law"
        CRIMINAL_LAW = "Criminal Law", "Criminal Law"
        FAMILY_LAW = "Family Law", "Family Law"
        TAX_LAW = "Tax Law", "Tax Law"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lawyer_profile')
    license_number = models.CharField(max_length=100)
    law_firm = models.ForeignKey(LawFirm, on_delete=models.SET_NULL, null=True, blank=True)
    practice_areas = models.CharField(blank=True,null=True,choices=PracticeAreas.choices,)  # List of practice areas
    years_of_experience = models.PositiveIntegerField(null=True,blank=True)
    education = models.TextField(null=True,blank=True)
    achievements = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.display_name

