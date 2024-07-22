from django.urls import path
from . import views

urlpatterns = [
    # post 首頁
    path("", views.index, name="posts"),
    # 閱讀每篇文章詳細
    path("<int:id>", views.post_detail, name="post_detail"),
    # 創建新頁面
    path("newpost", views.newPost, name="new_post"),
]
