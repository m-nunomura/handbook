from django.shortcuts import render

# django.viewsからgenericをインポート
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    #トップページのビュー

    '''
    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name: レンダリングするテンプレート   
    '''
    # index.htmlをレンダリングする
    template_name = "blogapp/index.html"