console.log("login.js")

document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();
    loginSubmit(event);
});

// 登入
function loginSubmit(event) {
    let url = window.location.href;
    let form = event.target;
    let formData = new FormData(form);
    let statusMsg = document.getElementById("login-status");

    fetch(url, {
        method: "POST",
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("登入成功");
                window.location.href = data.redirect_url;
            } else {
                console.log("登入失敗");
                statusMsg.textContent = "帳號或密碼錯誤";
                statusMsg.style.color = "#dc3545";
                statusMsg.style.display = 'block';
            }
        })
        .catch(error => {
            console.error('發生錯誤:', error);
        });
}