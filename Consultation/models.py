from django.db import models

from User.models import User

from LawFirm.models import LawFirm


class Consultation(models.Model):
    STATUS_CHOICES = [
        ('active', 'مفعلة'),
        ('inactive', 'غير مفعلة'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    law_firm = models.ForeignKey(LawFirm, on_delete=models.CASCADE)
    consultation_type = models.CharField(max_length=50, choices=[
        ('family', 'أسري'),
        ('administrative', 'إداري'),
        ('criminal', 'جنائي'),
        ('investment', 'استثمار'),
    ])
    content = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    response = models.TextField(blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"استشارة من {self.user.username} لمكتب {self.law_firm.name}"


class Consultant(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    law_firm = models.ForeignKey(LawFirm, on_delete=models.CASCADE, related_name='consultants')

