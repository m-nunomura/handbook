from django.shortcuts import render

# django.viewsからgenericをインポート
from django.views import generic

# modelsをインポート
from . import models

# Create your views here.

class IndexView(generic.ListView):
    #トップページのビュー

    '''
    投稿記事を一覧表示するのでListViewを継承する

    Attributes:
        template_name: レンダリングするテンプレート
        context_object_name: object_listキーの別名を設定
        queryset: データベースのクエリ   
    '''
    
    # index.htmlをレンダリングする
    template_name = "blogapp/index.html"

    # object_listキーの別名を設定
    context_object_name = "orderby_records"

    #モデルBlogPostのオブジェクトにorder_by()を適用してBlogPostのレコードを投稿日時の降順で並び替える
    queryset = models.BlogPost.objects.order_by("-posted_at")



class BlogDetail(generic.DeleteView):
    # 詳細ページのビュー

    '''
    投稿記事の詳細を表示するのでDetailViewを継承する

    Attributes:
        template_name: レンダリングするテンプレート
        Model: モデルのクラス
    '''

    # post.htmlをレンダリングする
    template_name = "blogapp/post.html"

    # クラス変数modelにモデルBlogPostを設定
    model = models.BlogPost
















    '''function'''
def index_view(request):
    # トップページのビュー
    '''
    テンプレートをレンダリングして戻り値として返す

    Parameters:
        request(HTTPRequest): クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト

    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''

    # モデルBlogPostのオブジェクトにorderby()を適用してBlogPostのレコードを投稿日時の降順で並べ替える
    records = models.BlogPost.objects.order_by("-posted_at")

    # render()：
    # 第1引数：HttpRequestオブジェクト
    # 第2引数：レンダリングするテンプレート
    # 第3引数：テンプレートに引き渡すdict型のデータ{任意のキー:クエリの結果（レコードのリスト）}
    return render(request,"blogapp/index.html",{"orderby_records":records})



def blog_detail(request,pk):
    # 詳細ページのビュー
    '''
    テンプレートをレンダリングして戻り値として返す

    Parameters:
        request(HTTPRequest): クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト

        pk(int): 投稿記事のレコードのid

    Returns(HttpResponse):
        テンプレートpost.htmlをレンダリングした結果
    '''

    # モデルのマネージャをBlogPost.objectsで参照し、get()を実行
    # 引数に指定したidのレコードを取得してrecordに格納
    record = models.BlogPost.objects.get(id=pk)

    # render():
    # 第1引数：HttpRequestオブジェクト
    # 第2引数：レンダリングするテンプレート
    # 第3引数：テンプレートに引き渡すdict型のデータ{任意のキー:get()で取得したレコード}
    return render(request,"blogapp/post.html",{"object":record})
