from django.urls import path
from . import views

# URLconfのURLパターンを逆引きできるように
# アプリ名を登録
app_name = "blogapp"

# URLパターンを老六するためのリスト
urlpatterns = [
    # http://ホスト名/以下のパスが""（無し）の場合
    # viewsモジュールのIndexViewを実行
    # URLパターン名は"index"
    path("", views.IndexView.as_view(), name="index"),
    # リクエストされたURLが「blog-detail/レコードのid/」の場合
    # viewsモジュールのBlogDetailを実行
    # URLパターン名は'blog_detail'
    path(
        # 詳細ページのURLは「blog-detail/レコードのid」
        "blog-detail/<int:pk>/",
        # viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        # URLパターンの名前を'blog_detail'にする
        name="blog_detail",
    ),
]
