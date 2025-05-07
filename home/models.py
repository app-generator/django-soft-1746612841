# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class System(models.Model):

    #__System_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    #__System_FIELDS__END

    class Meta:
        verbose_name        = _("System")
        verbose_name_plural = _("System")


class Patch(models.Model):

    #__Patch_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    package_id = models.CharField(max_length=255, null=True, blank=True)

    #__Patch_FIELDS__END

    class Meta:
        verbose_name        = _("Patch")
        verbose_name_plural = _("Patch")


class Mapping(models.Model):

    #__Mapping_FIELDS__
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    patch = models.ForeignKey(Patch, on_delete=models.CASCADE)
    version = models.CharField(max_length=255, null=True, blank=True)
    new_version = models.CharField(max_length=255, null=True, blank=True)

    #__Mapping_FIELDS__END

    class Meta:
        verbose_name        = _("Mapping")
        verbose_name_plural = _("Mapping")


class Organisation(models.Model):

    #__Organisation_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Organisation_FIELDS__END

    class Meta:
        verbose_name        = _("Organisation")
        verbose_name_plural = _("Organisation")


class Tenant(models.Model):

    #__Tenant_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    #__Tenant_FIELDS__END

    class Meta:
        verbose_name        = _("Tenant")
        verbose_name_plural = _("Tenant")



#__MODELS__END
