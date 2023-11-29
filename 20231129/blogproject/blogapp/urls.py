from django.urls import path
from . import views

# URLConfのURLパターンを逆引きできるようにアプリ名を登録
app_name = "blogapp"

# URLパターンを登録するためのリスト
urlpatterns = [
    
    # http(s)://ホスト名/以下のパスが""（無し）の場合
    # viewsモジュールのIndexViewを実行
    # URLパターン名は"index"
    path("",views.IndexView.as_view(),name="index"),
    
    # リクエストされたURLが「blog-detail/レコードのid」の場合
    # viewsモジュールのBlogDetailを実行
    # URLパターン名を"blog_detail"にする
    path("blog-detail/<int:pk>/",views.BlogDetail.as_view(),name="blog_detail"),











    ## function ##

    # http(s)://ホスト名/以下のパスが"func"の場合
    # viewsモジュールのindex_view()を実行
    # URLパターン名は"index"
    path("func/",views.index_view,name="index"),
    path("func/blog-detail/<int:pk>/",views.blog_detail,name="blog_detail"),
]