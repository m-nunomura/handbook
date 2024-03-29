from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

# django.viewsからgenericをインポート
from django.views import generic

# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy

# formsモジュールをインポート modelsモジュールをインポート
from . import forms,models,consts

# method_decoratorをインポート
from django.utils.decorators import method_decorator

# login_requiredをインポート
from django.contrib.auth.decorators import login_required

# Create your views here.

class IndexView(generic.ListView):
    # トップページのビュー

    # index.htmlをレンダリング
    template_name = "photo/index.html"

    # モデルBlogPostのオブジェクトにorder_by()を適用して投稿日時の降順で並べ替える
    queryset = models.PhotoPost.objects.order_by("-posted_at")

    # 1ページに表示するレコードの件数
    paginate_by = consts.ITEM_PER_PAGE


# デコレータにより、CreatePhotoViewへのアクセスはログインユーザに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required,name="dispatch")
class CreatePhotoView(generic.CreateView):
    # 写真投稿ページのビュー

    '''
    PhotoPostFormで定義されているモデルとフィールドと連携して投稿データをデータベースに登録する
    
    Attributes:
        form_class: モデルとフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベースの登録完了後のリダイレクト先
    '''

    # forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = forms.PhotoPostForms

    # レンダリングするテンプレート
    template_name = "photo/post_photo.html"

    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy("photo:post_done")


    def form_valid(self, form):
        # CreateViewクラスのform_valid()をオーバーライド

        '''
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う

        parameters:
            form(django.forms.Form): form_classに格納されているPhotoPostFormオブジェクト
        Return:
            HttpResponseRedirectオブジェクト:
                スーパークラスのform_valid()の戻り値を返すことで、success_urlで設定され散るURLにリダイレクトさせる
        '''

        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)

        # 投稿ユーザのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user

        # 投稿データをデータベースに登録
        postdata.save()

        # 戻り値はスーパークラスのform_valid()の戻り値（HttpResponseRedirect）
        return super().form_valid(form)
    

class PostSuccessView(generic.TemplateView):
    # 投稿完了ページのビュー

    '''
    Attributes:
        template_name: レンダリングするテンプレート
    '''

    # index.htmlをレンダリングする
    template_name = "photo/post_success.html"


class CategoryView(generic.ListView):
    # カテゴリページのビュー

    '''
    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''

    # imdex.htmlをレンダリングする
    template_name = "photo/index.html"

    # 1ページに表示するレコードの件数
    paginate_by = consts.ITEM_PER_PAGE_CATE

    def get_queryset(self):
        # クエリを実行する

        '''
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''

        # self.kwargsでキーワードの辞書を取得し、categoryキー値(Categorysテーブルのid)を取得
        category_id = self.kwargs["category"]

        # filter（フィールド名=id）で絞り込む
        categories = models.PhotoPost.objects.filter(category = category_id).order_by("-posted_at")

        # クエリによって取得されたレコードを返す
        return categories 
    
class UserView(generic.ListView):
    # ユーザの投稿一覧ページのビュー

    '''
    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''

    # index.htmlをレンダリングする
    template_name = "photo/index.html"

    # 1ページに表示するレコードの件数
    paginate_by = consts.ITEM_PER_PAGE_USER

    def get_queryset(self):
        # クエリを実行する

        '''
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する

        Retruns:
            クエリによって取得されたレコード
        '''

        # self.kwargsでキーワードの辞書を取得し、userキー値(ユーザテーブルのid)を取得
        user_id = self.kwargs["user"]

        # filter(フィールド名=id)で絞り込む
        user_list = models.PhotoPost.objects.filter(user=user_id).order_by("-posted_at")

        # クエリによって取得されたレコードを返す
        return user_list
    
class DetailView(generic.DetailView):
    # 詳細ページのビュー

    '''
    投稿記事の詳細を表示するのでDetailViewを継承する
    Attributes:
        template_name: レンダリングするテンプレート
        model: モデルのクラス    
    '''

    # detail.htmlをレンダリングする
    template_name = "photo/detail.html"

    # クラス変数modelにモデルPhotoPostを設定
    model = models.PhotoPost

class MypageView(generic.ListView):
    # マイページのビュー

    '''
    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''

    # mypage.htmlをレンダリングする
    template_name = "photo/mapage.html"

    # 1ページに表示するレコードの件数
    paginate_by = consts.ITEM_PER_PAGE_MYPAGE

    def get_queryset(self):
        # クエリを実行する

        '''
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する

        Return:
            クエリによって取得されたレコード
        '''

        # 現在ログインしているユーザ名はHttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞り込む
        queryset = models.PhotoPost.objects.filter(user=self.request.user).order_by("-posted_at")

        # クエリによって取得されたレコードを返す
        return queryset
    

class PhotoDeleteView(generic.DeleteView):
    # レコードの削除を行うビュー

    '''
    Attributes:
        model: モデル
        template_name: レンダリングするテンプレート
        success_url: 削除完了後のリダイレクト先のURL
    '''

    # 操作の対象はPhotoPost
    model = models.PhotoPost

    # photo_delete.htmlをレンダリングする
    template_name = "photo/photo_delete.html"

    # 処理完了後にマイページにリダイレクト
    success_url = reverse_lazy("photo:mypage")

    def delete(self,request,*args,**kwargs):
        # レコードの削除を行う

        '''
        Parameters:
            self: PhotoDeleteViewオブジェクト
            request: WSGIRequest(HttpRequest)オブジェクト
            args: 引数として渡される辞書(dict)
            Kwargs: キーワード月の辞書(dict){"pk":2}のようにレコードidが渡される

        Returns:
            HttpResponseRedirect(Xuccess_url)を渡してsaccess_urlにリダイレクト
        '''

        # スーパークラスのdelete()を実行
        return super().delete(request,*args,**kwargs)



#