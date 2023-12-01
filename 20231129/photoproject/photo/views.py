from django.shortcuts import render

# django.viewsからgenericをインポート
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    # トップページのビュー

    # index.htmlをレンダリング
    template_name = "photo/index.html"