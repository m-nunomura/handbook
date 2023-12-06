from django.db import models

# accountsアプリのmodelsをインポート
from accounts import models as accounts_models

# Create your models here.

class Category(models.Model):
    # 投稿する写真のカテゴリを管理するモデル

    # カテゴリ名のフィールド
    title = models.CharField(verbose_name="カテゴリ",
                              max_length=20)
    
    def __str__(self):
        #オブジェクトを文字列に変換して返す

        # Return(str): カテゴリ名
        return self.title
    

class PhotoPost(models.Model):
    # 投稿されたデータを管理するモデル

    # CustomUserモデルのuser_idとPhotoPostモデルを1対多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(accounts_models.CustomUser,verbose_name="ユーザ",on_delete=models.CASCADE)

    # CategoryモデルのtitleとPhotoPostモデルを1対多の関係で結びつける
    # Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.PROTECT)

    # タイトル用のフィールド
    title = models.CharField(verbose_name="タイトル",max_length=200)

    # コメント用のフィールド
    comment = models.TextField(verbose_name="コメント")

    # イメージのフィールド1
    image1 = models.ImageField(verbose_name="イメージ1",upload_to="photos")

    # イメージのフィールド2
    image2 = models.ImageField(verbose_name="イメージ2",upload_to="photos",blank=True,null=True)

    # 投稿日時のフィールド
    posted_at = models.DateTimeField(verbose_name="投稿日時",auto_now_add=True)

    def __str__(self):
        # オブジェクトを文字列に変換して返す

        # Retrun(str): 投稿記事のタイトル
        return self.title