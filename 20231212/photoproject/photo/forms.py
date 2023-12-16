from django.forms import ModelForm
from . import models

class PhotoPostForm(ModelForm):
    class Meta:
        model = models.PhotoPost
        fields = ["category","title","comment","image1","image2",]