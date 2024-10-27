# law_firms/models.py
from django.db import models
from User.models import User


class LawFirm(models.Model):
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
    practice_areas = models.JSONField()  # List of practice areas, e.g., civil, commercial, family, etc.

    def __str__(self):
        return self.name


class LawyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lawyer_profile')
    license_number = models.CharField(max_length=100)
    law_firm = models.ForeignKey(LawFirm, on_delete=models.SET_NULL, null=True, blank=True)
    practice_areas = models.JSONField()  # List of practice areas
    years_of_experience = models.PositiveIntegerField()
    education = models.TextField()
    achievements = models.TextField()

    def __str__(self):
        return self.user.display_name

