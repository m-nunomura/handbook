# 文字列を出力する関数
def hello():         # hello()関数の定義
    print('こんにちは')

hello()              # hello()関数を実行

# 引数を2つ受け取る関数
def show_hello(name1, name2): # 2つのパラメーターを設定
    print(name1 + 'さん、こんにちは!')
    print(name2 + 'さん、こんにちは!')

show_hello('山田', '鈴木')    # 引数を2つ設定して関数を呼び出す

# 引数を受け取り戻り値を返す関数
def return_hello(name1, name2):     # 2つのパラメーターを設定
    result = name1+ 'さん、' + name2 + 'さん、こんにちは!'
    return result                   # 処理した文字列を戻り値として返す

show = return_hello('山田', '鈴木') # 引数を2つ設定して関数を呼び出す
print(show)                         # 関数の戻り値を出力
