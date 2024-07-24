from django.db import models


# 文章結構
class Post(models.Model):
    id = models.AutoField(primary_key=True)  # 主鍵
    title = models.CharField(max_length=160)  # 標題
    content = models.TextField(null=True, blank=True)  # 內容
    create_at = models.DateTimeField(auto_now_add=True)  # 建立時間
    update_at = models.DateTimeField(auto_now=True)  # 更新時間

    def __str__(self) -> str:
        return self.title
