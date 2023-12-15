from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.


#'''
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "orderby_records"
    queryset = models.BlogPost.objects.order_by("-posted_at")
#'''



'''
def index_view(request):
    records = models.BlogPost.objects.order_by("-posted_at")
    context = {
        "orderby_records":records
    }
    return render(request,"blog/index.html",context)
'''
