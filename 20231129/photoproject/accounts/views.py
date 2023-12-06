from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from . import forms
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(generic.CreateView):
    # サインアップページのビュー

    # レンダリングするテンプレート
    template_name = "accounts/signup.html"

    # form.pyで定義したフォームのクラス
    form_class = forms.CustomUserCreateionForm

    #サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy("accounts:sigup_success")

    def form_valid(self, form):
        #CreateViewクラスのform_valid()をオーバーライド

        '''
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録を行う

        parameters:
            form_classに格納されているCustomUserCreateionFormオブジェクト
        Return:
            HttpResponseRedirectオブジェクト: スーパークラスのform_valid()の戻り値を返すことで、success_urlで設定されているURLにリダイレクトさせる
        '''

        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user

        #戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


class SignUpSuccessView(generic.TemplateView):
    # サインアップ完了ページのビュー

    # レンダリングするテンプレート
    template_name = "accounts/signup_success.html"