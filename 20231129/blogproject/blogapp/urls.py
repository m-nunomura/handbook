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

    # scienceカテゴリの一覧ページのURLパターン
    # scienceカテゴリの一覧ページのURLは「science-list」
    # viewsモジュールのScienceViewを実行
    # URLパターンの名前を"science_list"にする
    path("science-list/",views.ScienceView.as_view(),name="science_list"),

    # dailylifeカテゴリの一覧ページのURLパターン
    # dailylifeカテゴリの一覧ページのURLは「dailylife-list」
    # viewsモジュールのDailylifeViewを実行
    # URLパターンの名前を"dailylife_list"にする
    path("dailylife-list/",views.DailyView.as_view(),name="dailylife_list"),

    # musicカテゴリの一覧ページのURLパターン
    # musicカテゴリの一覧ページのURLは「music-list」
    # viewsモジュールのMusicViewを実行
    # URLパターンの名前を"music_list"にする
    path("music-list/",views.MusicView.as_view(),name="music_list"),







    ## function ##

    # http(s)://ホスト名/以下のパスが"func"の場合
    # viewsモジュールのindex_view()を実行
    # URLパターン名は"index"
    path("func/",views.index_view,name="index2"),

    # リクエストされたURLが「blog-detail/レコードのid」の場合
    # viewsモジュールのblog_detail()関数を実行
    # URLパターン名を"blog_detail"にする
    path("func/blog-detail/<int:pk>/",views.blog_detail,name="blog_detail2"),

    # scienceカテゴリの一覧ページのURLパターン
    # scienceカテゴリの一覧ページのURLは「science-list/」
    # viewsモジュールのscience_view()関数を実行
    # URLパターンの名前を"science_list"にする
    path("func/science-list/",views.science_view,name="science_list"),

    # dailylifeカテゴリの一覧ページのURLパターン
    # dailylifeカテゴリの一覧ページのURLは「dailylife-list/」
    # viewsモジュールのdailylife_view()関数を実行
    # URLパターンの名前を"dailylife_list"にする
    path("func/dailylife-list/",views.dailylife_view,name="dailylife_list"),

    # musicカテゴリの一覧ページのURLパターン
    # musicカテゴリの一覧ページのURLは「music-list/」
    # viewsモジュールのmusic_view()関数を実行
    # URLパターンの名前を"music_list"にする
    path("func/music-list/",views.music_view,name="music_list"),
]