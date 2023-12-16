from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms,models,consts
# Create your views here.

#'''
class IndexView(generic.ListView):
    template_name = "photo/index.html"
    queryset = models.PhotoPost.objects.order_by("-posted_at")
    paginate_by = consts.IMAGE_PAGENATE

@method_decorator(login_required,name="dispatch")
class CreatePhotoView(generic.CreateView):
    template_name = "photo/post_photo.html"
    form_class = forms.PhotoPostForm
    success_url = reverse_lazy("photo:post_done")

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)


class PostSuccessView(generic.TemplateView):
    template_name = "photo/post_success.html"

class CategoryView(generic.ListView):
    template_name = "photo/index.html"
    paginate_by = consts.CATE_PAGENATE
    
    def get_queryset(self):
        category_id = self.kwargs["category"]
        categories = models.PhotoPost.objects.filter(category=category_id).order_by("-posted_at")
        return categories

class UserView(generic.ListView):
    template_name = "photo/index.html"
    paginate_by = consts.USER_PAGENATE
    
    def get_queryset(self):
        user_id = self.kwargs["user"]
        user_list = models.PhotoPost.objects.filter(user=user_id).order_by("-posted_at")
        return user_list
    
class DetailView(generic.DetailView):
    template_name = "photo/detail.html"
    model = models.PhotoPost

class MypageView(generic.ListView):
    template_name = "photo/mypage.html"
    paginate_by = consts.MYPAGE_PAGENATE
    
    def get_queryset(self):
        queryset = models.PhotoPost.objects.filter(user=self.request.user).order_by("-posted_at")
        return queryset

class PhotoDeleteView(generic.DeleteView):
    template_name = "photo/photo_delete.html"
    model = models.PhotoPost
    success_url = reverse_lazy("photo:mypage")

    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)








#'''

'''
def index_view(request):
    return render(request,"photo/index.html")
'''