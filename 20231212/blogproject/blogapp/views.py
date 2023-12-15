from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMessage
from . import models,consts,forms
# Create your views here.


#'''
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "orderby_records"
    queryset = models.BlogPost.objects.order_by("-posted_at")
    paginate_by = consts.PAGINATE

class BlogDetail(generic.DetailView):
    template_name = "blog/post.html"
    model = models.BlogPost

class ScienceView(generic.ListView):
    template_name = "blog/science_list.html"
    context_object_name = "science_records"
    queryset = models.BlogPost.objects.filter(category="science").order_by("-posted_at")
    paginate_by = consts.PAGINATE_CATE

class DailylifeView(generic.ListView):
    template_name = "blog/dailylife_list.html"
    context_object_name = "dailylife_records"
    queryset = models.BlogPost.objects.filter(category="dailylife").order_by("-posted_at")
    paginate_by = consts.PAGINATE_CATE

class MusicView(generic.ListView):
    template_name = "blog/music_list.html"
    context_object_name = "music_records"
    queryset = models.BlogPost.objects.filter(category="music").order_by("-posted_at")
    paginate_by = consts.PAGINATE_CATE    

class ContactView(generic.FormView):
    template_name = "blog/contact.html"
    form_class = forms.ContactForm
    success_url = reverse_lazy("blogapp:contact")

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        title = form.cleaned_data["title"]
        message = form.cleaned_data["message"]
        subject = "お問い合わせ：{}".format(title)
        message = "送信者：{0}\nメールアドレス：{1}\nタイトル：{2}\nメッセージ：{3}".format(name,email,title,message)
        from_email = "admin@example.com"
        to_list = ["admin@example.com"]
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,)
        message.send()
        messages.success(self.request,"お問い合わせは正常に送信されました。")
        return super().form_valid(form)

#'''



'''
def index_view(request):
    records = models.BlogPost.objects.order_by("-posted_at")
    paginator = Paginator(records,consts.PAGINATE)
    page_number = request.GET.get("page",1)
    pages = paginator.page(page_number)
    context = {
        "orderby_records":pages,
        "page_obj":pages,
    }
    return render(request,"blog/index.html",context)

def blog_detail(request,pk):
    records = models.BlogPost.objects.get(id=pk)
    context = {
        "object":records,
    }
    return render(request,"blog/post.html",context)

def science_view(request):
    records = models.BlogPost.objects.filter(category="science").order_by("-posted_at")
    paginator = Paginator(records,consts.PAGINATE_CATE)
    page_number = request.GET.get("page",1)
    pages = paginator.page(page_number)
    context = {
        "science_records":pages,
        "page_obj":pages,
    }
    return render(request,"blog/science_list.html",context)

def dailylife_view(request):
    records = models.BlogPost.objects.filter(category="dailylife").order_by("-posted_at")
    paginator = Paginator(records,consts.PAGINATE_CATE)
    page_number = request.GET.get("page",1)
    pages = paginator.page(page_number)
    context = {
        "dailylife_records":pages,
        "page_obj":pages,
    }
    return render(request,"blog/dailylife_list.html",context)

def music_view(request):
    records = models.BlogPost.objects.filter(category="music").order_by("-posted_at")
    paginator = Paginator(records,consts.PAGINATE_CATE)
    page_number = request.GET.get("page",1)
    pages = paginator.page(page_number)
    context = {
        "music_records":pages,
        "page_obj":pages,
    }
    return render(request,"blog/music_list.html",context)

def contact_view(request):
    if request.method == "GET":
        form = forms.ContactForm()
        context = {
            "form":form,
        }
        return render(request,"blog/contact.html",context)
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            title = form.cleaned_data["title"]
            message = form.cleaned_data["message"]
            subject = "お問い合わせ：{}".format(title)
            message = "送信者：{0}\nメールアドレス：{1}\nタイトル：{2}\nメッセージ：{3}".format(name,email,title,message)
            from_email = "admin@example.com"
            to_list = ["admin@example.com"]
            message = EmailMessage(subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list,)
            message.send()
            messages.success(request,"お問い合わせは正常に送信されました。")
            return redirect("blogapp:contact")
'''

