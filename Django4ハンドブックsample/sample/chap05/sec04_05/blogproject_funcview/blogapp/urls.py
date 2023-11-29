from django.urls import path
from . import views

# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'blogapp'

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのindex_view()関数を実行
    # URLパターン名は'index'
    path('', views.index_view, name='index'),
    
    # リクエストされたURLが「blog-detal/レコードのid/」の場合
    # viewsモジュールのblog_detail()関数を実行
    # URLパターン名は'blog_detail'
    path(
        # 詳細ページのURLは「blog-detail/レコードのid/」
        'blog-detail/<int:pk>/',
        # viewsモジュールのblog_detail()関数を実行
        views.blog_detail,
        # URLパターンの名前を'blog_detail'にする
        name='blog_detail'
        ),
]
