from django.shortcuts import render
from django.views import generic
# Create your views here.


'''
class IndexView(generic.TemplateView):
    template_name = "blog/index.html"
'''


def index_view(request):
    return render(request,"blog/index.html")