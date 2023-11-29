from django.contrib import admin

# Register your models here.

# modelsからBlogPostクラスをインポート
from .models import BlogPost

# Django管理サイトにBlogPostを登録する
admin.site.register(BlogPost)
