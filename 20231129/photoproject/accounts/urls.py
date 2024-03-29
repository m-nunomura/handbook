from django.urls import path

# viewsモジュールをインポート
from . import views

# viewsをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_view

# URLパターンを逆引きできるように名前を付ける
app_name = "accounts"

# URLパターンを登録する変数
urlpatterns = [
    # サインアップページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対してviewsモジュールのSignUpViewをインスタンス化する
    path("signup/",views.SignUpView.as_view(),name="signup"),

    # サインアップ完了ページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup_success/」へのアクセスに対して、viewsモジュールのSignUpSuccessViewをインスタンス化する
    path("signup_success/",views.SignUpSuccessView.as_view(),name="sigup_success"),

    # ログインページの表示
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、django.contrib.auth.views.LoginViewをインスタンス化してログインページを表示する
    path("login/",auth_view.LoginView.as_view(template_name="accounts/login.html"),name="login"),

    # ログアウトを実行
    # 「http(s)://<ホスト名>/logout/」へのアクセスに対して、django.contrib.auth.views.LogoutViewをインスタンス化してログアウトさせる
    path("logout/",auth_view.LogoutView.as_view(template_name="accounts/logout.html"),name="logout"),
]