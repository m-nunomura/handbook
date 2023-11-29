from django.urls import path
from . import views

# URLConfのURLパターンを逆引きできるようにアプリ名を登録
app_name = "funcblogapp"

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが""（無し）の場合
    # viewsモジュールのindex_viewを実行
    # URLパターン名は"index"
    path("",views.index_view,name="index"),
]