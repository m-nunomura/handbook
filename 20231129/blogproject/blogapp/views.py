

# django.viewsからgenericをインポート
from django.http import HttpResponse
from django.views import generic

# models、consts、formsをインポート
from . import models,consts,forms

# django.urlからreverse_lazyをインポート
from django.urls import reverse_lazy

# django.contribからmessagesをインポート
from django.contrib import messages

# django.core.mailモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage

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

    paginate_by = consts.ITEM_PER_PAGE



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


class ScienceView(generic.ListView):
    # 科学（science）カテゴリの記事を一覧表示するビュー

    # science_list.htmlをレンダリングする
    template_name = "blogapp/science_list.html"

    # クラス変数modelにモデルBlogPostを設定
    model = models.BlogPost

    # object_listキーの別名を設定
    context_object_name = "science_records"

    # categor="science"のレコードを抽出して投稿日時の降順で並べ替える
    queryset = models.BlogPost.objects.filter(category="science").order_by("-posted_at")

    # 1ページに表示するレコードの件数
    paginate_by = consts.ITEM_PER_PAGE_CATE



class DailyView(generic.ListView):
    # 日常（dailylife）カテゴリの記事を一覧表示するビュー

    # dailylife_list.htmlをレンダリングする
    template_name = "blogapp/dailylife_list.html"

    # クラス変数modelにモデルBlogPostを設定
    model = models.BlogPost

    # object_listキーの別名を設定
    context_object_name = "dailylife_records"

    # category="dailylife"のレコードを抽出して投稿日時の降順で並べ替える
    queryset = models.BlogPost.objects.filter(category="dailylife").order_by("-posted_at")

    # 1ページに表示するレコードの件数
    paginate_by = consts.ITEM_PER_PAGE_CATE



class MusicView(generic.ListView):
    # 音楽（music）カテゴリの記事を一覧表示するビュー

    # music_list.htmlをレンダリングする
    template_name = "blogapp/music_list.html"

    # クラス変数modelにモデルBlogPostを設定
    model = models.BlogPost

    # object_listキーの別名を設定
    context_object_name = "music_records"

    # category="music"のレコードを抽出して投稿日時の降順で並べ替える
    queryset = models.BlogPost.objects.filter(category="music").order_by("-posted_at")

    # 1ページに表示するレコードの件数
    paginate_by = consts.ITEM_PER_PAGE_CATE



class ContactView(generic.FormView):
    # 問い合わせページを表示する

    '''
    フォームで入力されたデータを取得し、メールの作成と送信を行う
    '''

    # contact.htmlをレンダリングする
    template_name = "blogapp/contact.html"
    
    # クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = forms.ContactForm

    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy("blogapp:contact")

    def form_valid(self, form):
        # FormViewクラスのform_valid()をオーバーライド

        '''
        フォームのバリデーションを通過したデータがPOSTされたときに呼ばれる
        メール送信を行う

        parameters:
            form(objet): ContactFormのオブジェクト

        Return:
            HttpResponseRedirectのオブジェクト
            オブジェクトをインスタンス化するとsuccess_urlで設定されているURLにリダイレクトされる
        '''

        # フォームに入力されたデータをフィールド名を指定して取得
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        title = form.cleaned_data["title"]
        message = form.cleaned_data["message"]

        # メールのタイトルの書式を設定
        subject = "お問い合わせ：{}".format(title)
        # フォームの入力データの書式を設定
        message = "送信者名：{0}\nメールアドレス：{1}\nタイトル：{2}\nメッセージ：{3}".format(name,email,title,message)

        # メールの送信元のアドレス
        from_email = "admin@example.com"
        # 送信先のメールアドレス
        to_list = ["admin@example.com",]
        # EmailMessageオブジェクトを生成
        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,)

        # EmailMessageクラスのsend()でメールサーバからメールを送信
        message.send()

        # 送信完了後に表示するメッセージ
        messages.success(self.request,"お問い合わせは正常に送信されました。")
        
        # 戻り値はスーパークラスのform?valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)












    '''function'''

from django.shortcuts import render

# redirectを追加
from django.shortcuts import redirect

# Paginatorをインポート
from django.core.paginator import Paginator

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

    # Paginator(レコード,1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records,consts.ITEM_PER_PAGE)

    # GET陸エスのURLにpageパラメータがある場合はその値を取得する
    # pageパラメータがない場合はデフォルトで1を返すようにする
    page_number = request.GET.get("page",1)

    # page()メソッドの引数にページ番号を設定し、該当ページのレコードを取得する
    pages = paginator.page(page_number)

    # render()：
    # 第1引数：HttpRequestオブジェクト
    # 第2引数：レンダリングするテンプレート
    # 第3引数：テンプレートに引き渡すdict型のデータ{任意のキー:クエリの結果（レコードのリスト）}
    return render(request,"blogapp/index.html",{"orderby_records":pages,"page_obj":pages})



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
    records = models.BlogPost.objects.get(id=pk)

    # render():
    # 第1引数：HttpRequestオブジェクト
    # 第2引数：レンダリングするテンプレート
    # 第3引数：テンプレートに引き渡すdict型のデータ{任意のキー:get()で取得したレコード}
    return render(request,"blogapp/post.html",{"object":records})



def science_view(request):
    # scienceカテゴリのビュー
    '''
    science_list.htmlをレンダリングして戻り値として返す

    Parameters:
        request(HTTPRequest): クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponce):
        render()でテンプレートをレンダリングした結果
    '''

    # モデルBlogPostのオブジェクトにfilter()を適用してscienceカテゴリを抽出
    # order_by()を適用してレコードを投稿日時の降順で並び替える
    records = models.BlogPost.objects.filter(category="science").order_by("-posted_at")

    # Paginator(レコード,1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records,consts.ITEM_PER_PAGE_CATE)

    # GETリクエストのURLにpageパラメータがある場合はその値を取得する
    # pageパラメータがない場合はデフォルトで1を返すようにする
    page_number = request.GET.get("page",1)

    # page()メソッドの引数にページ番号を設定し、該当ページのレコードを取得する
    pages = paginator.page(page_number)
    
    # render():
    # 第1引数：HttpRequestオブジェクト
    # 第2引数：レンダリングするテンプレート
    # 第3引数：テンプレートに引き渡すdict型のデータ{キーは"orderby_records":リクエストされたページのレコードのリスト}
    return render(request,"blogapp/science_list.html",{"orderby_records":pages,"science_records":pages})




def dailylife_view(request):
    # dailylifeカテゴリのレビュー
    '''
    dailylife_list.htmlをレンダリングして戻り値として返す

    Parameters:
        request(HTTPRequest): クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
        Returns(HTTPResponce):
            render()でテンプレートをレンダリングした結果
    '''

    # モデルBlogPostのオブジェクトにfilter()を適用してdailylifeカテゴリを抽出
    # order_by()を適用してレコードを投稿日時の降順で並べ替える
    records = models.BlogPost.objects.filter(category="dailylife").order_by("-posted_at")

    # Paginator(レコード,1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records,consts.ITEM_PER_PAGE_CATE)

    # GETリクエストのURLにpageパラメータがある場合はその値を取得する
    # pageパラメータがない場合はデフォルトで1を返すようにする
    page_number = request.GET.get("page",1)

    # page()メソッドの引数にページ番号を設定し、該当ページのレコードを取得する
    pages = paginator.page(page_number)

    # render():
    # 第1引数：HttpRequestオブジェクト
    # 第2引数：レンダリングするテンプレート
    # 第3引数：テンプレートに引き渡すdict型のデータ{キーは"orderby_records":リクエストされたページのレコードのリスト}
    return render(request,"blogapp/dailylife_list.html",{"object_records":pages,"dailylife_records":pages})



def music_view(request):
    # musicカテゴリのビュー
    '''
    music_list.htmlをレンダリングして戻り値として返す

    Parameters:
        request(HTTPRequest): クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''

    # モデルBlogPostのオブジェクトにfilter()を適用してmusicカテゴリを抽出
    # order_by()を適用してレコードを投稿日時の降順で並べ替える
    records = models.BlogPost.objects.filter(category="music").order_by("-posted_at")

    # Paginator(レコード,1ページあたりのレコード数)でページに分割
    paginator = Paginator(records,consts.ITEM_PER_PAGE_CATE)

    # GETリクエストのURLにpageパラメータがある場合はその値を取得する
    # pageパラメータがない場合はデフォルトで1を返すようにする
    page_number = request.GET.get("page",1)

    # page()メソッドの引数にページ番号を設定し、該当ページのレコードを取得する
    pages = paginator.page(page_number)

    # render():
    # 第1引数：HTTPRequestオブジェクト
    # 第2引数：レンダリングするテンプレート
    # 第3引数：テンプレートに引き渡すdict型のデータ{キーは"orderby_records":リクエストされたページのレコードのリスト}
    return render(request,"blogapp/music_list.html",{"object_records":pages,"music_records":pages})



def contact_view(request):
    # Contactページのビュー

    '''
    contact.htmlをレンダリングして戻り値として返す

    Parameters:
        request(HTTPRequest): クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト

    Returns(HTTPResponce):
        Contactページへのアクセス時: render()でテンプレートをレンダリングした結果
        sendボタンがクリックされた場合: メールの送信処理完了後、Contactページにリダイレクトする
    '''

    # Contactページへのアクセスがあった場合（リクエストがGETの場合）
    # render()でテンプレートをレンダリングする
    if request.method == "GET":

        # ContactFormオブジェクトを生成
        form = forms.ContactForm()

        # render():
        # 第1引数: HTTPRequestオブジェクト
        # 第2引数: レンダリングするテンプレート
        # 第3引数: テンプレートに引き渡すdict型のデータ{キーは"form":ContactFormオブジェクト}
        return render(request,"blogapp/contact.html",{"form":form})
    
    # 送信ボタン（send）がクリックされた場合（リクエストがPOSTの場合）
    else:

        # ContactFormオブジェクトを生成（引数はPOSTされたフォームデータ）
        form = forms.ContactForm(request.POST)

        # POSTされたフォームのデータがバリデーションを通過しているか確認
        if form.is_valid():

            # フォームに入力されたデータをフィールド名を指定して取得
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            title = form.cleaned_data["title"]
            message = form.cleaned_data["message"]

            # メールのタイトルの書式を設定
            subject = "お問い合わせ：{}".format(title)

            # フォームの入力データの書式を設定
            message = "送信者：{0}\nメールアドレス：{1}\nタイトル：{2}\nメッセージ：{3}".format(name,email,title,message)

            # メールの送信元アドレス（Gmail）
            from_email = "admin@example.com"

            # 送信先のメールアドレス
            to_list = ["admin@example.com",]

            # EmailMessageオブジェクトを生成
            message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list)

            # EmailMessageクラスのsend()でメールサーバからメールを送信
            message.send()

            # 送信完了語に表示するメッセージ
            messages.success(request,"お問い合わせは正常に送信されました。")

            # Contactページにリダイレクトする
            return redirect("blogapp:contact")
    return