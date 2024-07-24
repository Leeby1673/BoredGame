console.log("js 連接成功");

document.getElementById('post-form').addEventListener('submit', function (event) {
    event.preventDefault();
    submitPost();
});

function submitPost() {
    const form = document.getElementById('post-form');
    const formData = new FormData(form)
    const csrftoken = getCookie('csrftoken');

    // 發送 POST 請求到後端服務器
    fetch('/posts/newpost', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData
        // body: JSON.stringify({
        //     title: formData.get('title'),
        //     content: formData.get('content'),
        // })
    })
        // 接收後端返回的響應
        .then(response => response.json())
        // 處理後端返回的資料
        .then(data => {
            if (data.message === 'new post successful') {
                console.log(data.post_id)
                window.location.href = '/posts'
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('發生錯誤, 抱歉我菜');
        });
}

// 取得 csrf cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}