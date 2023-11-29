# すべての要素がint型のリスト
number = [1,2,3,4,5]

# すべての要素がstr型のリスト
words = ['Django', 'Web','インターネット']

# ｓｔｒ型、int型、float型が混在したリスト
data = ['身長', 160, '体重', 40.5]


sweets = []                # 空のリストをブラケットで作る
sweets.append('ティラミス')    # 要素を追加
print(sweets)              # 出力： ['ティラミス']
sweets.append('チョコエクレア') # 要素を追加
print(sweets)              # 出力：['ティラミス', 'チョコエクレア']

# リストのインデクシング
sweets = ['ティラミス', 'チョコエクレア', 'クレームブリュレ']
print(sweets[0])   # 出力：ティラミス
print(sweets[1])   # 出力：'チョコエクレア'
print(sweets[2])   # 出力：'クレームブリュレ'

# リストをイテレートする
for count in [0, 1, 2, 3, 4]:
    print(count)