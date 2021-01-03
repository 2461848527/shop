
// 用来处理导航条的
function FrontBase() {}


FrontBase.prototype.run = function () {
    var self = this;
    self.listenAuthBoxHover();
};

// 监听hover(鼠标靠近，这里是做登录后下拉列表的事件)事件
FrontBase.prototype.listenAuthBoxHover = function () {
    // 登录后的下拉列表的最外部盒子
    var authBox = $(".auth-box");
    // 登录后的下拉列表的内部盒子
    var userMoreBox = $(".user-more-box");
    // 鼠标靠近登录后的用户下拉列表盒子
    authBox.hover(function () {
        userMoreBox.show();
    },function () {
        userMoreBox.hide();
    });
};


// 把auth.js文件代码复制过来
// 用来处理登录和注册的
function Auth() {
    var self = this;
    // 选择登录和注册的最外部盒子
    self.maskWrapper = $('.mask-wrapper');
    // 选择只包含登录和注册模块的盒子
    self.cardFront = $('.card-front');
    // 选择只包含登录和注册模块的盒子
    self.cardBack = $('.card-back');

}

Auth.prototype.run = function () {
    var self = this;
    self.listenShowHideEvent();
    // self.listenSwitchEvent();
    // self.listenSigninEvent();
    // self.listenImgCaptchaEvent();
    // self.listenSignupEvent();
};
// 登录页展示
Auth.prototype.showLoginEvent = function () {
    window.location.href = 'user/login/'
};
// 注册页展示
Auth.prototype.showRegEvent = function () {
    window.location.href = 'user/register/'
};


Auth.prototype.listenShowHideEvent = function () {
    var self = this;
    // 首页中登录按钮
    var signinBtn = $('.signin-btn');
    // 首页中注册按钮
    var signupBtn = $('.signup-btn');
    // 首页中登录按钮的点击事件
    signinBtn.click(function () {
        // 调用展示登录、注册盒子的事件
        self.showLoginEvent();
    });

    signupBtn.click(function () {
        // 调用展示登录、注册盒子的事件
        self.showRegEvent();

    });

};


$(function () {
    var frontBase = new FrontBase();
    frontBase.run();
});
