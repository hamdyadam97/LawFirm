

from django.db.models.signals import post_save
from django.dispatch import receiver

from LawFirm.models import LawFirm
from User.models import User, LawyerProfile, CustomerProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == User.UserTypeChoices.LAW_FIRM:
            LawFirm.objects.create(user=instance)
        elif instance.user_type == User.UserTypeChoices.LAWYER:
            LawyerProfile.objects.create(user=instance)
        elif instance.user_type == User.UserTypeChoices.CUSTOMER:
            CustomerProfile.objects.create(user=instance)
