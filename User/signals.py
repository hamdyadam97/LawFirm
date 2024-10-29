

from django.db.models.signals import post_save
from django.dispatch import receiver

from LawFirm.models import LawFirm, LawyerProfile
from .models import User, CustomerProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(instance.user_type)
        if instance.user_type == User.UserTypeChoices.LAW_FIRM:
            print(instance.user_type)
            LawFirm.objects.create(user=instance)
        elif instance.user_type == User.UserTypeChoices.LAWYER:
            print(instance.user_type)
            LawyerProfile.objects.create(user=instance)
        elif instance.user_type == User.UserTypeChoices.CUSTOMER:
            CustomerProfile.objects.create(user=instance)
