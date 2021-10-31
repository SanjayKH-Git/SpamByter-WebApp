from django.contrib import admin
from .models import GenUsers, SpamUsers
# Register your models here.

admin.site.register(GenUsers)
admin.site.register(SpamUsers)
