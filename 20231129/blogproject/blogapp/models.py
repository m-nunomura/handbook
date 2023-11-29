from django.db import models
from . import consts

# Create your models here.

class BlogPost(models.Model):
    # モデルクラス

    # タイトル用のフィールド
    title = models.CharField(
        verbose_name="タイトル",    # フィールドのタイトル
        max_length=200              # 最大文字数は200
    )
    
    # 本文用のフィールド
    content = models.TextField(
        verbose_name="本文"         # フィールドのタイトル
    )

    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name="投稿日時",    # フィールドのタイトル
        auto_now_add=True           # 日時を自動追加
    )

    # カテゴリのフィールド
    category = models.CharField(
        verbose_name="カテゴリ",    # フィールドのタイトル
        max_length=50,              # 最大文字数は50
        choices=consts.CATEGORY     # categoryフィールドにはCATEGORYの要素のみを登録
    )


    def __str__(self):
        '''
        Django管理サイトでデータを表示する際に識別名として
        投稿記事のタイトル（titleフィールドの値）を表示するために必要

        Returns(str)：投稿記事のタイトル
        '''
        return self.title