from django.shortcuts import render
# django.views.genericからListView、DetailViewをインポート
from django.views.generic import ListView, DetailView
# モデルBlogPostをインポート
from .models import BlogPost

class IndexView(ListView):
    '''トップページのビュー
    
    投稿記事を一覧表示するのでListViewを継承する
    
    Attributes:
      template_name: レンダリングするテンプレート
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数を設定
    paginate_by = 4

class BlogDetail(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承する
     Attributes:
      template_name: レンダリングするテンプレート
      Model: モデルのクラス
    '''
    # post.htmlをレンダリングする
    template_name ='post.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost

class ScienceView(ListView):
    '''科学(science)カテゴリの記事を一覧表示するビュー
    
    '''
    # science_list.htmlをレンダリングする
    template_name ='science_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'science_records'
    # category='science'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='science').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class DailylifeView(ListView):
    '''日常(dailylife)カテゴリの記事を一覧表示するビュー
    
    '''
    # dailylife_list.htmlをレンダリングする
    template_name ='dailylife_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'dailylife_records'
    # category='dailylife'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class MusicView(ListView):
    '''音楽(music)カテゴリの記事を一覧表示するビュー
    
    '''
    # music_list.htmlをレンダリングする
    template_name ='music_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'music_records'
    # category='music'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='music').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2
