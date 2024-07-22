from django.contrib import admin
from .models import Post


# 讓管理介面可以看到 models 欄位資訊
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "create_at",
        "update_at",
    )


admin.site.register(Post, PostAdmin)
