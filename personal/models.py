from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class PersonalDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
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

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, verbose_name='user', null=True)
    content = models.TextField(blank=True)

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Education(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    agree = models.CharField(verbose_name='Derece', max_length=100, null=False, blank=False)
    city = models.CharField(verbose_name='City', max_length=55)
    school = models.CharField(verbose_name='School', max_length=255)
    starter_date = models.DateField()
    end_date = models.DateField()
    content = models.TextField(verbose_name='Content')

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Education, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.agree


class Experience(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    jobTitle = models.CharField(verbose_name='JobTitle', max_length=100, null=False, blank=False)
    city = models.CharField(verbose_name='City', max_length=55)
    employer = models.CharField(verbose_name='Employer', max_length=255)
    starter_date = models.DateField()
    end_date = models.DateField()
    content = models.TextField(verbose_name='Content')

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Experience, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.jobTitle


class Ability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    name = models.CharField(max_length=100, verbose_name='Name')
    level = models.IntegerField(verbose_name='level')

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Ability, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.name


class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    language = models.CharField(max_length=100, verbose_name='Name')
    level = models.IntegerField(verbose_name='level')

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.language


class Reference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    company = models.CharField(max_length=100, verbose_name='company')
    person = models.CharField(max_length=100, verbose_name='person')
    telephone = models.CharField(max_length=55, verbose_name='Telephone')
    email = models.EmailField()

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Reference, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.company


class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    name = models.CharField(max_length=100, verbose_name='Name')

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Hobby, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.name


class Course(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    name = models.CharField(verbose_name='Derece', max_length=100, null=False, blank=False)
    institution = models.CharField(verbose_name='City', max_length=255)
    starter_date = models.DateField()
    end_date = models.DateField()
    content = models.TextField(verbose_name='Content')

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.name


class Achievement(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    content = models.TextField(verbose_name='Content')

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Achievement, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.id


class Publication(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    content = models.TextField(verbose_name='Content')

    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Publication, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.id
