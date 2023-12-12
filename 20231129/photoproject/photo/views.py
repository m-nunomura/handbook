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