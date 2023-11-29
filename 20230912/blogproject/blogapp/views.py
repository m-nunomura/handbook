from django.shortcuts import render

# django.views.genericからListView、DetailViewをインポート
from django.views.generic import ListView, DetailView

# Create your views here.

# django.views.genericからListViewをインポート
from django.views.generic import ListView

# モデルBlogPostをインポート
from .models import BlogPost


class IndexView(ListView):
    """トップページビュー

    投稿記事を一覧表示するのでListViewを継承する

    Attributes:
        template_name:レンダリングするテンプレート
        context_object_name:object_listキーの別名を設定
        queryset:データベースのクエリ
    """

    # index.htmlをレンダリングする
    template_name = "index.html"
    # object_listキーの別名を設定
    context_object_name = "orderby_records"
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並び変える
    queryset = BlogPost.objects.order_by("-posted_at")


class BlogDetail(DetailView):
    """詳細ページのビュー

    投稿記事の詳細を表示するのでDetailViewを継承する
    Attributes:
        template_name:レンダリングするテンプレート
        Model:モデルのクラス
    """

    # post.htmlをレンダリングする
    template_name = "post.html"
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
