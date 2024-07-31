console.log("js 連接成功");

document.addEventListener('DOMContentLoaded', function (event) {
    event.preventDefault();
    readPost();
    deletePost();
})

// 點擊文章 dom, 閱讀完整文章
function readPost() {
    document.querySelector('.post-container').addEventListener('click', function (event) {
        // 檢查點擊元素
        if (event.target.closest('.dropdown')) {
            return;
        }

        if (event.target.closest('.postarea')) {
            // data-post-id 在這取值, 會轉換成駝峰式命名 postId
            const postId = event.target.closest('.postarea').dataset.postId;
            window.location.href = `/posts/${postId}`;
        }
        // else 可增加錯誤處理 console.error('Post ID not found for this post.');
    });
}

// 刪除文章
function deletePost() {
    document.querySelectorAll('.delete-button').forEach(button => {
        button.addEventListener('click', function () {
            const url = this.dataset.deleteUrl;
            console.log("fetch url: ", url)

            // 送出請求
            fetch(url, {
                method: 'POST',
                // header
            })
                // 接收響應
                .then(response => response.json())
                .then(data => {
                    if (data.message === 'delete OK') {
                        location.reload()
                    }
                })
                // 錯誤發生
                .catch(error => {
                    console.log("發生錯誤: ", error)
                })
        });
    });
}