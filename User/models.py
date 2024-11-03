import re
import uuid
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager



def validate_username_user(username):
    pattern = re.compile("^(?=[a-zA-Z0-9._]{3,20}$)(?!.*[_.]{2})[^_.].*[^_.]$")
    if pattern.match(username):
        return username
    else:
        raise ValidationError("The username field should be between 3 and 20 characters in length and may contain "
                              "characters, numbers, or special characters (_.), but not at the beginning or end.")\



from django.contrib.auth.models import UserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    def get_by_natural_key(self, email):
        return self.get(**{f'{self.model.USERNAME_FIELD}__iexact': email })

    def create_user(self, email, username, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)



def upload_to_profile_pic(instance, filename):
    return f'uploads/profile/{ uuid.uuid4() }/{ filename }'


class User(AbstractBaseUser, PermissionsMixin):

    class UserGenderChoices(models.TextChoices):
        MALE = 'male', "Male"
        FEMALE = 'female', "Female"
        PREFERE_NOT_TO_ANSWER = 'prefer_not_to_answer', "Prefere not to answer"

    class UserTypeChoices(models.TextChoices):
        LAW_FIRM = 'law_firm', _("Law Firm")
        LAWYER = 'lawyer', _("Lawyer")
        CUSTOMER = 'customer', _("Customer")

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=50,
        unique=True,
        help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator,validate_username_user],
        error_messages={
            'unique': _("This username already exists."),
        },
    )
    user_type = models.CharField(max_length=50, choices=UserTypeChoices.choices, default=UserTypeChoices.CUSTOMER)

    display_name = models.CharField(max_length=150)
    email = models.EmailField(_('email address'),unique=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='upload_to_profile_pic',)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_code = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=25, choices=UserGenderChoices.choices, blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_deactivated = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_phone_verified = models.BooleanField(default=False)
    phone_country_code = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )



    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.display_name

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @cached_property
    def token(self):
        return RefreshToken.for_user(self)


class LawFirmUser(User):
    # Fields specific to law firms
    firm_name = models.CharField(max_length=255)
    firm_license_number = models.CharField(max_length=100)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.display_name
