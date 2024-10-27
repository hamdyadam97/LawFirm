from django.db import models

from LawFirm.models import LawFirm


class Job(models.Model):
    law_firm = models.ForeignKey(LawFirm, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    benefits = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    application_link = models.URLField()

    def __str__(self):
        return self.title
