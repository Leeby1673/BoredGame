from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import json


@csrf_exempt
def index(request):
    return render(request, "post.html")


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
            print(f"標題: {title} / 內容: {content}")

            # 丟 res 給前端
            return JsonResponse({"message": "new post successful"})
        # 錯誤是 JSONDecodeError 的話
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    # GET 請求
    else:
        return render(request, "newpost.html")
