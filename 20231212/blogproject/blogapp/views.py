from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.


#'''
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "orderby_records"
    queryset = models.BlogPost.objects.order_by("-posted_at")

class BlogDetail(generic.DetailView):
    template_name = "blog/post.html"
    model = models.BlogPost



#'''



'''
def index_view(request):
    records = models.BlogPost.objects.order_by("-posted_at")
    context = {
        "orderby_records":records,
    }
    return render(request,"blog/index.html",context)

def blog_detail(request,pk):
    records = models.BlogPost.objects.get(id=pk)
    context = {
        "object":records,
    }
    return render(request,"blog/post.html",context)
'''
