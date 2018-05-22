"""Imports."""
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save


class StaffProfile(models.Model):
    """
    This model defines both staff and volunteer users.

    This does not define children in the program
    """

    user = models.OneToOneField(
        User,
        related_name='user_profile',
        on_delete=models.CASCADE
    )
    about_you = models.TextField(
        max_length=3000,
        blank=True,
        null=True)
    country_of_residence = models.CharField(
        max_length=120,
        blank=True,
        null=True)
    city_of_residience = models.CharField(
        max_length=120,
        blank=True,
        null=True)
    email = models.EmailField(
        blank=True, 
        null=True)
    phone = models.CharField(
        max_length=24, 
        blank=True, 
        null=True)
    location = models.CharField(
        max_length=180, 
        blank=True, 
        null=True)
    user_language_spoken = models.CharField(
        max_length=120, 
        blank=True, 
        null=True)
    user_language_spoken_other = models.CharField(
        max_length=120,
        blank=True,
        null=True)
    user_language_written = models.CharField(
        max_length=120,
        blank=True,
        null=True)
    user_language_written_other = models.CharField(
        max_length=120,
        blank=True,
        null=True)
  
    role = MultiSelectField(
        choices=(('heartbeat_admin',
                  'Heartbeat Admin (Gives Sitewide Access: Use Caution'),
                 ('manager_cambodia', 'Manager: Cambodia'),
                 ('manager_china', 'Manager: China'),
                 ('manager_india', 'Manager: India'),
                 ('manager_uganda', 'Manager: Uganda'),
                 ('coordinator_cambodia_education',
                  'Coordinator: Cambodia Education'),
                 ('coordinator_cambodia_education_rangsei',
                  'Coordinator: Cambodia Education Rangsei Village'),
                 ('coordinator_cambodia_education_sokhem',
                  'Coordinator: Cambodia Education Sokhem Village'),
                 ('coordinator_cambodia_education_sokhem_sibling',
                  'Coordinator: Cambodia Education Sokhem Sibling'),
                 ('coordinator_cambodia_education_ary',
                  'Coordinator: Cambodia Education Ary Village'),
                 ('coordinator_cambodia_foster_care',
                  'Coordinator: Cambodia Foster Care'),
                 ('coordinator_cambodia_healing_homes',
                  'Coordinator: Cambodia Healing Homes'),
                 ('coordinator_cambodia_medical',
                  'Coordinator: Cambodia Medical'),
                 ('coordinator_cambodia_nutrition',
                  'Coordinator: Cambodia Nutrition'),
                 ('coordinator_cambodia_safe_haven',
                  'Coordinator: Cambodia Safe Haven'),
                 ))

    is_active = models.BooleanField(default=True)

    @classmethod
    def active(cls):
        """Class method."""
        return cls.objects.filter(is_active=True)

    def __str__(self):
        """Class String magic."""
        return self.user.username


@receiver(post_save, sender=User)
def staff_profile_hook(sender, **kwargs):
    pass
