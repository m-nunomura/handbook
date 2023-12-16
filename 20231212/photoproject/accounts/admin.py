from django.contrib import admin
from . import models
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id","username",)
    list_display_links = ("id","username",)

admin.site.register(models.CustomUser,CustomUserAdmin)