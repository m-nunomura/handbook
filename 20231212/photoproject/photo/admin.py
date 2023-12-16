from django.contrib import admin
from . import models
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","title",)
    list_display_links = ("id","title",)

class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ("id","title",)
    list_display_links = ("id","title",)

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.PhotoPost,PhotoPostAdmin)