console.log("js 連接成功");

document.addEventListener('DOMContentLoaded', function () {
    clickPost();
})

// 點擊文章 dom, 導向完整文章內容
function clickPost() {
    document.querySelector('.post-container').addEventListener('click', function (event) {
        // 檢查點擊元素
        if (event.target.closest('.dropdown')) {
            return;
        }

        if (event.target.closest('.postarea')) {
            const postId = event.target.closest('.postarea').dataset.postId;
            window.location.href = `/posts/${postId}`;
        }
        // else 可增加錯誤處理 console.error('Post ID not found for this post.');
    });
}