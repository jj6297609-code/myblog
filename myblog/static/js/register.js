$(function () {
    function bindCaptchaBtnClick() {
        $("#captcha_btn").click(function (event) {
            let $this = $(this);
            let email = $("input[name='email']").val();
            if (!email) {
                alert("请先输入邮箱！");
                return;
            }
            $this.off('click')

            $.ajax("/auth/captcha?email=" + email, {
                method: "GET",
                success: function (result) {
                    console.log(result);
                },
                error: function (error) {
                    console.log(error);
                }
            })
            let countdown = 6;
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text('获取');
                    clearInterval(timer);
                    bindCaptchaBtnClick()
                } else {
                    $this.text(countdown + 's');
                    countdown--;
                }
            }, 1000)
        })
    }

    bindCaptchaBtnClick();
})
