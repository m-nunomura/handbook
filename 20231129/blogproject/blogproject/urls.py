"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# include()関数を使うためincludeを追加
from django.urls import path,include

# プロジェクトのURLパターンを登録するリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスがadmin/にマッチングした場合
    # admin.site.urlsを呼び出し、Django管理サイトを表示する
    path("admin/", admin.site.urls),
    path("func/",include("funcblogapp.urls")),

    # http(s)://ホスト名/へのアクセスはblogappの
    # URLConf(urls.py)を呼び出す
    path("",include("blogapp.urls")),
    
]
