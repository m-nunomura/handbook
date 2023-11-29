# 辞書を作成
menu = {'朝食' : 'シリアル',
        '昼食' : '牛丼',
        '夕食' : 'トマトのパスタ' }
print(menu) # {'朝食': 'シリアル', '昼食': '牛丼', '夕食': 'トマトのパスタ'}

#　辞書の要素をキーを使って参照する 
print(menu['朝食'])

# 作成済みの辞書に要素を追加する
menu['おやつ'] = 'ドーナッツ'
print(menu)

# 登録済みの値を変更する
menu['おやつ'] = 'いちご大福'
print(menu)

# キーを指定して要素を削除する
del menu['おやつ']
print(menu)

# キーをイテレートして列挙する
setting= {
          '設定1' : 'メール送信',
          '設定2' : 'リクエスト',
          '設定3' : 'レスポンス'
        }

for key in setting:
    print(key)

# 辞書の値をイテレートする
for val in setting.values():
    print(val)

# 辞書の値をリストとして取得する
val = setting.values()
print(val)

# 辞書の要素をすべて取得する
val = setting.items()
print(val)

# 辞書のキーと値をイテレートする
for key, value in setting.items():
    # 書式を設定して出力
    print('「{}」は{}です。'.format(key, value))

