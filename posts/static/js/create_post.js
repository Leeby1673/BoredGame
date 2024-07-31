console.log("js 連接成功");

document.getElementById('post-form').addEventListener('submit', function (event) {
    event.preventDefault();
    submitPost();
});

function submitPost() {
    const form = document.getElementById('post-form');
    const formData = new FormData(form)
    let url = window.location.href;
    const csrftoken = Cookies.get('csrftoken');

    // 發送 POST 請求到後端服務器
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
        // 接收後端返回的響應
        .then(response => response.json())
        // 處理後端返回的資料
        .then(data => {
            if (data.message === 'new post successful') {
                console.log(data.post_id)
                window.location.href = '/posts'
            } else if (data.message === 'update post successful')
                console.log("更新成功 id:", data.post_id)
            window.location.href = `/posts/${data.post_id}`
        })
        .catch(error => {
            console.error('Error:', error);
            alert('發生錯誤, 抱歉我菜');
        });
}