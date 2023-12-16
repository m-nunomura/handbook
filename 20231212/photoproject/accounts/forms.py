from django.contrib.auth.forms import UserCreationForm
from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ("username","email","password1","password2",)