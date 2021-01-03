// 把auth.js文件代码复制过来
// 用来处理登录和注册的
function Auth() {
    var self = this;
    // 选择登录和注册的最外部盒子
    self.maskWrapper = $('.mask-wrapper');
    // // 选择只包含登录和注册模块的盒子
    // self.scrollWrapper = $(".card-front");

}

Auth.prototype.run = function () {
    var self = this;
    // self.listenShowHideEvent();
    // // self.listenSwitchEvent();
    self.listenSigninEvent();
    // self.listenImgCaptchaEvent();
    self.listenSignupEvent();
};
// // 监听图形验证码的事件
// Auth.prototype.listenImgCaptchaEvent = function () {
//     // 定位验证码图片
//     var imgCaptcha = $('.img-captcha');
//     // 通过点击验证码图片，来更改验证码图片
//     imgCaptcha.click(function () {
//         // 添加查询参数，会自动重新获取图片验证码
//         imgCaptcha.attr("src","/account/img_captcha/"+"?random="+Math.random())
//     });
// };
// 监听登录事件
Auth.prototype.listenSigninEvent = function () {
    var self = this;
    // 获取登录盒子
    var signinGroup = $('#index');

    // 通过“立即登录”提交按钮，来提交从前端获取的数据
    signinGroup.click(function () {
        // // 获取用户输入的电话号
        // var email = emailInput.val();
        // // 获取用户输入的密码
        // var password = passwordInput.val();
        // // 获取是否记住我的状态
        // var remember = rememberInput.prop("checked");
        // 给后台路径为’/account/login/‘发送post请求
        $.ajax({
            url: '/user/login/',
            type: 'POST',
            data: $('#index_Form').serialize(),
            dataType: 'JSON',
            success:function (res) {
                // alert('已签收返回数据包')
                if (res.status == 0){
                    // alert(res.form)
                    location.href = res.form  //跳转主页
                }else if (res.status == 1){
                    alert('信息错误!')
                    // 提示错误
                    // $.each(res.form, function (key, value) {
                    //     // alert(value[0])
                    //     document.getElementById("id_spinner").classList.remove('spinner-grow', 'spinner-grow-sm');
                    //     $('#' + key + '_error-feedback').html(value[0]);
                    // })
                }else {
                    alert('505')
                    $('#password_error-feedback').html(res.form);
                }
            }
        });
    });
};

// 获取元素，再绑定注册点击事件
// eg.10
Auth.prototype.listenSignupEvent = function () {
    // 获取注册模块
    var signupGroup = $('#register');
    // // 在注册模块中找’立即注册按钮‘
    // var submitBtn = signupGroup.find('submit-btn');
    // 点击’立即注册‘提交按钮后的事件
    signupGroup.click(function (event) {
        // 阻止默认表单提交的行为
        // event.preventDefault();
        // alert('111')
        // 提取相应的input标签
        // 在注册模块中找name等于telephone的文本框
        // var emailInput = signupGroup.find("input[name='logemail']");
        // // 在注册模块中找name等于username的文本框
        // var usernameInput = signupGroup.find("input[name='logname']");
        // // 在注册模块中找name等于password1的文本框
        // var password1Input = signupGroup.find("input[name='logpass']");
        // // 在注册模块中找name等于password2的文本框
        // var password2Input = signupGroup.find("input[name='logpass2']");
        //
        // // 提取相应的值
        // var email = emailInput.val();
        // var username = usernameInput.val();
        // var password1 = password1Input.val();
        // var password2 = password2Input.val();

        // alert($('#reg_Form').serialize())
        // 拿到数据以后发送给服务器，提交数据
        $.ajax({
            url: '/user/register/',
            type: 'POST',
            data: $('#reg_Form').serialize(), // 获取所有的字段数据 + csrf token
            dataType: 'JSON',
            success:function (res) {
               if (res.status == 0){
                   // alert(res.form)
                    location.href = res.form  //跳转主页
                }else if (res.status == 1){
                    alert('信息错误!')
                    // 提示错误
                    // $.each(res.form, function (key, value) {
                    //     // alert(value[0])
                    //     document.getElementById("id_spinner").classList.remove('spinner-grow', 'spinner-grow-sm');
                    //     $('#' + key + '_error-feedback').html(value[0]);
                    // })
                }else {
                    alert('505')
                    $('#password_error-feedback').html(res.form);
                }
                // if (res.status == 0){
                    // location.href = res.form  //跳转主页
                // }else if (res.status == 1){
                //     alert('11')
                    //提示错误
                    // $.each(res.form, function (key, value) {
                    //     // alert(value[0])
                    //     document.getElementById("id_spinner").classList.remove('spinner-grow', 'spinner-grow-sm');
                    //     $('#' + key + '_error-feedback').html(value[0]);
                    // })
                // }else {
                //     $('#password_error-feedback').html(res.form);
                // }
            }
        })
    });
};


$(function () {
    var auth = new Auth();
    auth.run();
});



// 给attemplate添加时间过滤器
$(function () {
    // 如果有加载arttemplate
    if(window.template){
        template.defaults.imports.timeSince = function (dateValue) {
            var date = new Date(dateValue);
            var datets = date.getTime(); // 得到的是毫秒的
            var nowts = (new Date()).getTime(); //得到的是当前时间的时间戳
            var timestamp = (nowts - datets)/1000; // 除以1000，得到的是秒
            if(timestamp < 60) {
                return '刚刚';
            }
            else if(timestamp >= 60 && timestamp < 60*60) {
                minutes = parseInt(timestamp / 60);
                return minutes+'分钟前';
            }
            else if(timestamp >= 60*60 && timestamp < 60*60*24) {
                hours = parseInt(timestamp / 60 / 60);
                return hours+'小时前';
            }
            else if(timestamp >= 60*60*24 && timestamp < 60*60*24*30) {
                days = parseInt(timestamp / 60 / 60 / 24);
                return days + '天前';
            }else{
                var year = date.getFullYear();
                var month = date.getMonth();
                var day = date.getDay();
                var hour = date.getHours();
                var minute = date.getMinutes();
                return year+'/'+month+'/'+day+" "+hour+":"+minute;
            }
        }
    }
});