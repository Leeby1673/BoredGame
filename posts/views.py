from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import Post
from .forms import PostForm

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


# 新增文章
@login_required
@csrf_protect
def create_post(request):
    # POST 請求
    if request.method == "POST":
        # 創建一個 表單 實例, 並用請求中的資料補滿它
        print("給出訊息: ", request.POST)
        form = PostForm(request.POST)
        # 驗證表單
        if form.is_valid():
            # 成功
            try:
                form.save()
                print("新增文章成功")
                return JsonResponse({"message": "new post successful"})
            # 意料之外的錯誤：
            except Exception as e:
                print("出現意外錯誤")
                return JsonResponse({"error": f"創建表單時出錯: {e}"}, status=500)
        # 驗證出錯
        else:
            print("驗證失敗: ", form.errors)
            errors = form.errors.as_json()
            return JsonResponse(
                {"error": "表單無效, 請檢查輸入內容", "form_errors": errors},
                status=400,
            )

    # GET 請求
    else:
        # 返回空表單
        form = PostForm()
        return render(
            request,
            "create_post.html",
            {"form": form},
        )


# 閱讀文章
@csrf_exempt
def read_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(
        request,
        "read_post.html",
        {"post": post},
    )


# 更新文章
@csrf_exempt
def update_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    # POST 請求
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            try:
                form.save()
                print("更新文章成功")
                return JsonResponse(
                    {"message": "update post successful", "post_id": post.id},
                )
            except Exception as e:
                print("出事了阿伯")
                return JsonResponse({"error": f"更新表單時出錯: {e}"}, status=500)
        else:
            # 驗證失敗
            print("驗證失敗: ", form.errors)
            errors = form.errors.as_json()
            return JsonResponse(
                {"error": "更新無效, 請檢查輸入內容", "form_errors": errors},
                status=400,
            )

    # GET 請求
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "create_post.html",
        {"form": form},
    )


# 刪除文章
@csrf_exempt
def delete_post(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, id=pk)
        post.delete()
        print("刪除文章成功")
        return JsonResponse({"message": "delete OK"})
    else:
        return JsonResponse({"message": "delete not OK"})


# 搜尋文章
@csrf_exempt
def search_post(request):
    query = request.GET.get("query", "")
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    return render(
        request,
        "post.html",
        {"posts": results},
    )


# 施工中
@csrf_exempt
def wip(request):
    return render(request, "wip.html")
