# UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# modelsをインポート
from . import models


class CustomUserCreateionForm(UserCreationForm):
    # UserCreationFormのサブクラス

    class Meta:
        # UserCreationFormのインナークラス

        '''
        Attributes:
            model: 連携するUserモデル
            fields: フォームで使用するフィールド
        '''

        # 連携するUserモデルを設定
        model = models.CustomUser
        # フォームで使用するフィールドを設定
        # ユーザ名、メールアドレス、パスワード、パスワード（確認用）
        fields = ("username","email","password1","password2",)