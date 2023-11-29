from django.contrib import admin
# modelsをインポート
from . import models

# Register your models here.

# Django管理サイトにBlogPostを登録する
admin.site.register(models.BlogPost)