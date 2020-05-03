from django.db import models

# Create your models here.
from django.utils import timezone


class PersonalDetail(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    surname = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(verbose_name='email')
    address = models.CharField(max_length=255, verbose_name='adress', null=True, blank=True)
    city = models.CharField(max_length=55, verbose_name='city', null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    birthOfPlace = models.CharField(max_length=55, null=True, blank=True)
    drivingLicence = models.CharField(max_length=55, null=True, blank=True)
    gender = models.CharField(max_length=55, null=True, blank=True)
    maritalStatus = models.CharField(max_length=55, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(PersonalDetail, self).save(*args, **kwargs)
