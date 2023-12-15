from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from . import models,consts
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
'''
