"""
URL configuration for photoproject project.

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
from django.urls import path,include    #include追加

# auth.viewsをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # photo.urlsへのURLパターン
    path("",include("photo.urls")),

    # accounts.urlへのURLパターン
    path("",include("accounts.urls")),

    # パスワードリセットのためのURLパターン
    # PasswordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載
    
    # パスワードリセット申し込みページ
    path("password_reset/",auth_view.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="password_reset"),

    # メール送信完了ページ
    path("password_reset/done/",auth_view.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),

    # パスワードリセットページ
    path("reset/<uidb64>/<token>/",auth_view.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),

    # パスワードリセット完了ページ
    path("reset/done/",auth_view.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),
]