from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout
from . import forms
# Create your views here.

class SignUpView(generic.CreateView):
    template_name = "accounts/signup.html"
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("accounts:signup_success")

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)
    
class SignupSuccessView(generic.TemplateView):
    template_name = "accounts/signup_success.html"

def logout_view(request):
    logout(request)
    return render(request,"accounts/logout.html")
