console.log("js 連接成功");
document.getElementById('post-form').addEventListener('submit', function (event) {
    event.preventDefault();
    submitPost();
});

function submitPost() {
    // const title = document.getElementById('title').value;
    // const content = document.getElementById('content').value;
    const form = document.getElementById('post-form');
    const formData = new FormData(form)

    // 發送 POST 請求到後端服務器
    fetch('/posts/newpost', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title: formData.get('title'),
            content: formData.get('content'),
        })
    })
        // 接收後端返回的響應
        .then(response => response.json())
        // 處理後端返回的資料
        .then(data => {
            console.log(data);
            if (data.message === 'new post successful') {
                window.location.href = '/posts'
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('發生錯誤, 抱歉我菜');
        });
}