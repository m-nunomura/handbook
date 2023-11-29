# redirectを追加
from django.shortcuts import render, redirect
# Paginatorをインポート
from django.core.paginator import Paginator
# モデルBlogPostをインポート
from .models import BlogPost
# formsモジュールからContactFormをインポート
from .forms import ContactForm
# django.contribからmesseagesをインポート
from django.contrib import messages
# django.core.mailモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage

def index_view(request):
    '''トップページのビュー    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    records = BlogPost.objects.order_by('-posted_at')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 4)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', 1)
    # page()メソッドの引数にページ番号を設定し、
    # 該当ページのレコードを取得する
    pages = paginator.page(page_number)
    # render():
    # 第1引数: HTTPRequestオブジェクト
    # 第2引数: レンダリングするテンプレート
    # 第3引数: テンプレートに引き渡すdict型のデータ
    #         {任意のキー : リクエストされたページのレコードのリスト}
    return render(
        request, 'index.html', {'orderby_records': pages})

def blog_detail(request, pk):
    '''詳細ページのビュー
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
      pk(int):
          投稿記事のレコードのid
    
    Returns(HTTPResponse):
        テンプレートpost.htmlをレンダリングした結果
    '''
    # モデルのマネージャーをBlogPost.objectsで参照し、get()を実行
    # 引数に指定したidのレコードを取得してrecordに格納
    record = BlogPost.objects.get(id=pk)
    # render():
    # 第1引数: HTTPRequestオブジェクト
    # 第2引数: レンダリングするテンプレート
    # 第3引数: テンプレートに引き渡すdict型のデータ
    #         {任意のキー : get()で取得したレコード)}
    return render(
        request, 'post.html', {'object': record})

def science_view(request):
    '''scienceカテゴリのビュー    
    science_list.htmlをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルBlogPostのオブジェクトにfilter()を適用してscienceカテゴリを抽出
    # order_by()を適用してレコードを投稿日時の降順で並べ替える
    records = BlogPost.objects.filter(category='science'
                                      ).order_by('-posted_at')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 2)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', 1)
    # page()メソッドの引数にページ番号を設定し、該当ページのレコードを取得する
    pages = paginator.page(page_number)
    # render():
    # 第1引数: HTTPRequestオブジェクト
    # 第2引数: レンダリングするテンプレート
    # 第3引数: テンプレートに引き渡すdict型のデータ
    #         {キーは'orderby_records':リクエストされたページのレコードのリスト}
    return render(
        request, 'science_list.html', {'orderby_records': pages})

def dailylife_view(request):
    '''dailylifeカテゴリののビュー    
    dailylife_list.htmlをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルBlogPostのオブジェクトにfilter()を適用してdailylifeカテゴリを抽出
    # order_by()を適用してレコードを投稿日時の降順で並べ替える
    records = BlogPost.objects.filter(category='dailylife'
                                      ).order_by('-posted_at')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 2)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', 1)
    # page()メソッドの引数にページ番号を設定し、該当ページのレコードを取得する
    pages = paginator.page(page_number)
    # render():
    # 第1引数: HTTPRequestオブジェクト
    # 第2引数: レンダリングするテンプレート
    # 第3引数: テンプレートに引き渡すdict型のデータ
    #         {キーは'orderby_records':リクエストされたページのレコードのリスト}
    return render(
        request, 'dailylife_list.html', {'orderby_records': pages})

def music_view(request):
    '''musicカテゴリのビュー    
    music_list.htmlをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルBlogPostのオブジェクトにfilter()を適用してmusicカテゴリを抽出
    # order_by()を適用してレコードを投稿日時の降順で並べ替える
    records = BlogPost.objects.filter(category='music'
                                      ).order_by('-posted_at')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 2)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', 1)
    # page()メソッドの引数にページ番号を設定し、該当ページのレコードを取得する
    pages = paginator.page(page_number)
    # render():
    # 第1引数: HTTPRequestオブジェクト
    # 第2引数: レンダリングするテンプレート
    # 第3引数: テンプレートに引き渡すdict型のデータ
    #         {キーは'orderby_records': リクエストされたページのレコードのリスト}
    return render(
        request, 'music_list.html', {'orderby_records': pages})

def contact_view(request):
    '''Contactページのビュー    
    contact.htmlをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        Contactページへのアクセス時:
            render()でテンプレートをレンダリングした結果
        Sendボタンがクリックされた場合
            メールの送信処理完了後、Contactページにリダイレクトする
    '''
    # Contactページへのアクセスがあった場合(リクエストがGETの場合)
    # render()でテンプレートをレンダリングする
    if request.method == 'GET':
        # ContactFormオブジェクトを生成
        form = ContactForm()
        # render():
        # 第1引数: HTTPRequestオブジェクト
        # 第2引数: レンダリングするテンプレート
        # 第3引数: テンプレートに引き渡すdict型のデータ
        #         {キーは'form': ContactFormオブジェクト}
        return render(request, "contact.html", {'form': form})
    # 送信ボタン（Send)がクリックされた場合(リクエストがPOSTの場合)
    else:
        # ContactFormオブジェクトを生成(引数はPOSTされたフォームデータ)
        form = ContactForm(request.POST)
        # POSTされたフォームのデータがバリデーションを通過しているかを確認
        if form.is_valid():
            # フォームに入力されたデータをフィールド名を指定して取得
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            # メールのタイトルの書式を設定
            subject = 'お問い合わせ: {}'.format(title)
            # フォームの入力データの書式を設定
            message = \
              '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
              .format(name, email, title, message)
            # メールの送信元のアドレス(Gmail)
            from_email = 'xxxxxxxx@gmail.com'
            # 送信先のメールアドレス(Gmail)
            to_list = ['xxxxxxxx@gmail.com']
            # EmailMessageオブジェクトを生成
            message = EmailMessage(subject=subject,
                                   body=message,
                                   from_email=from_email,
                                   to=to_list,
                                   )
            # EmailMessageクラスのsend()でメールサーバーからメールを送信
            message.send()
            # 送信完了後に表示するメッセージ
            messages.success(
              request, 'お問い合わせは正常に送信されました。')
            # Contactページにリダイレクトする
            return redirect('blogapp:contact')