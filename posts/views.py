from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
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


# 完整文章
@csrf_exempt
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(
        request,
        "post_detail.html",
        {"post": post},
    )


# 新增文章
@csrf_protect
def newPost(request):
    # POST 請求
    if request.method == "POST":
        # 創建一個 表單 實例, 並用請求中的資料補滿它
        print("給出訊息: ", request.POST)
        form = PostForm(request.POST)
        # 驗證表單
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"meaasge": "new post successful"}, status=201)
            # 意料之外的錯誤：
            except Exception as e:
                print("出現意外錯誤")
                return JsonResponse({"error": f"創建表單時出錯: {e}"}, status=500)
        # 驗證表單出錯
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
        return render(request, "newpost.html", {"form": form})
