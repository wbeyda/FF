from django.contrib import admin
from django_use_email_as_username.admin import BaseUserAdmin

from .models import User, Profile, Certification, Mental_Health_Test, Care

admin.site.register(User, BaseUserAdmin)
admin.site.register(Profile)
admin.site.register( Certification)
admin.site.register(Mental_Health_Test)
admin.site.register( Care)
