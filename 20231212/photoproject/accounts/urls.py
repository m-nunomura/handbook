from django.urls import path,include
from django.contrib.auth import views as auth_view
from . import views

app_name = "accounts"

#'''
urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("signup_success/",views.SignupSuccessView.as_view(),name="signup_success"),
    path("login/",auth_view.LoginView.as_view(template_name="accounts/login.html"),name="login"),
    path("logout/",views.logout_view,name="logout")
]