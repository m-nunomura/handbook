from django.urls import path,include
from . import views

app_name = "photo"

#'''
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("post/",views.CreatePhotoView.as_view(),name="post"),
    path("post_done/",views.PostSuccessView.as_view(),name="post_done"),
    path("photos/<int:category>/",views.CategoryView.as_view(),name="photos_cat")
]
#'''


'''
urlpatterns = [
    path("",views.index_view,name="index"),
]
'''