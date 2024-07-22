from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import json

# 視圖函式, 返回一個 response or error


# 首頁
@csrf_exempt
def index(request):
    posts = Post.objects.all()
    return render(
        request,
        "post.html",
        {"posts": posts},
    )


# 完整文章
@csrf_exempt
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(
        request,
        "post_detail.html",
        {"post": post},
    )


# 新增網頁
@csrf_exempt
def newPost(request):
    # POST請求
    if request.method == "POST":
        # 錯誤處理
        try:
            # 讀取 JSON
            data = json.loads(request.body)
            title = data.get("title")
            content = data.get("content")
            print(f"標題: {title}, 內容: {content}")

            # 對資料庫新增文章
            post = Post.objects.create(title=title, content=content)

            # 丟 res 給前端, 帶 post_id 給前端
            return JsonResponse({"message": "new post successful", "post_id": post.id})
        # 錯誤是 JSONDecodeError：
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        # 意料之外的錯誤：
        except Exception as e:
            print("出現意外錯誤")
            return JsonResponse({"error": str(e)}, status=500)
    # GET 請求
    else:
        return render(request, "newpost.html")
