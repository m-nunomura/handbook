from django.shortcuts import render

def index_view(request):
    '''トップページのビュー
    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
     
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
		'''
    return render(request, 'index.html')