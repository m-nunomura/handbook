from django.shortcuts import render

# Create your views here.
def index_view(request):
    # トップページのビュー
    '''
    Parameters:
        request(HTTPRequest): クライアントからのリクエスト情報
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    return render(request,"funcblogapp/index.html")