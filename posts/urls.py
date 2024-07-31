from django.urls import path
from . import views

urlpatterns = [
    # 首頁
    path("", views.index, name="posts"),
    # 新增文章路由 C
    path("create-post", views.create_post, name="create_post"),
    # 閱讀文章路由 R
    path("<int:pk>", views.read_post, name="read_post"),
    # 更新文章路由 U
    path("<int:pk>/edit", views.update_post, name="update_post"),
    # 刪除文章路由 D
    path("<int:pk>/delete", views.delete_post, name="delete_post"),
    # 搜尋文章路由
    path("search", views.search_post, name="search_post"),
    # 施工中路由
    path("wip1", views.wip, name="wip1"),
    path("wip2", views.wip, name="wip2"),
]
