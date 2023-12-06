from django . forms import ModelForm
from . import models

class PhotoPostForms(ModelForm):
    # ModelFormのサブクラス

    class Meta:
        # ModelFormsのインナークラス
        
        '''
        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''
        model = models.PhotoPost
        fields = ("category","title","comment","image1","image2",)