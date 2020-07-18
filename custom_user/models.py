from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(BaseUser):
    objects = BaseUserManager()

class Profile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField()
    pic = models.FileField(upload_to='uploads/%Y/%m/%d/', default='', blank=True)
    organization = models.CharField(max_length=100)

    ROLE_CHOICES = (
        ('Client', 'Client'),
        ('Business', 'Business')
    )

    role = models.CharField(max_length=8, choices=ROLE_CHOICES, default='Client')
    certification = models.ForeignKey('Certification', on_delete=models.CASCADE)
    resume = models.FileField()
    background = models.CharField(max_length=100)
    care = models.ForeignKey('Care', on_delete=models.CASCADE)
    stability_index = models.IntegerField()
    mental_health_scores = models.IntegerField()
    mental_health_tests = models.ForeignKey('Mental_Health_Tests', on_delete=models.CASCADE)
    sentence = models.CharField(max_length=100)
    release_date = models.DateField()

    JOB_STATUS_CHOICE = (
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed')
    )
    job_status = models.CharField(max_length=10, choices=JOB_STATUS_CHOICE, default='Unemployed')

    def __str__(self):
        return self.last_name +' '+ self.first_name


class Certification(models.Model):
    pass


class Mental_Health_Tests(models.Model):
    pass


class Care(models.Model):
    pass