$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	// var error_check = false;

    $('#log_name').blur(function() {
		check_user_name2();
	});

    $('#log_pass').blur(function() {
		check_user_pass2();
	});

	$('#logname').blur(function() {
		check_user_name();
	});

	$('#logpass').blur(function() {
		check_pwd();
	});

	$('#logpass2').blur(function() {
		check_cpwd();
	});

	$('#logemail').blur(function() {
		check_email();
	});

	// $('#allow').click(function() {
	// 	if($(this).is(':checked'))
	// 	{
	// 		error_check = false;
	// 		$(this).siblings('span').hide();
	// 	}
	// 	else
	// 	{
	// 		error_check = true;
	// 		$(this).siblings('span').html('请勾选同意');
	// 		$(this).siblings('span').show();
	// 	}
	// });
    // 判断是否输入用户时，是否输入用户名
    function check_user_name2(){
		var len = $('#log_name').val().length;
		if(len<5||len>20)
		{
			$('#log_name').next().next().html('请输入用户名')
			$('#log_name').next().next().show();
			error_name = true;
		}
		else
		{
			$('#log_name').next().next().hide();
			error_name = false;
		}
	}
    // 判断是否输入用户登入时，是否输入密码
	function check_user_pass2(){
		var len = $('#log_pass').val().length;
		if(len<5||len>20)
		{
			$('#log_pass').next().next().html('请输入您的密码')
			$('#log_pass').next().next().show();
			error_name = true;
		}
		else
		{
			$('#log_pass').next().next().hide();
			error_name = false;
		}
	}

	function check_user_name(){
		var len = $('#logname').val().length;
		if(len<5||len>20)
		{
			$('#logname').next().next().html('请输入5-20个字符的用户名')
			$('#logname').next().next().show();
			error_name = true;
		}
		else
		{
			$('#logname').next().next().hide();
			error_name = false;
		}
	}

	function check_pwd(){
		var len = $('#logpass').val().length;
		if(len<8||len>20)
		{
			$('#logpass').next().next().html('密码最少8位，最长20位')
			$('#logpass').next().next().show();
			error_password = true;
		}
		else
		{
			$('#logpass').next().next().hide();
			error_password = false;
		}
	}


	function check_cpwd(){
		var pass = $('#logpass').val();
		var cpass = $('#logpass2').val();

		if(pass!=cpass)
		{
			$('#logpass2').next().next().html('两次输入的密码不一致')
			$('#logpass2').next().next().show();
			error_check_password = true;
		}
		else
		{
			$('#logpass2').next().next().hide();
			error_check_password = false;
		}

	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#logemail').val()))
		{
			$('#logemail').next().next().hide();
			error_email = false;
		}
		else
		{
			$('#logemail').next().next().html('你输入的邮箱格式不正确')
			$('#logemail').next().next().show();
			error_check_password = true;
		}

	}


	// $('#reg_form').submit(function() {
	// 	check_user_name();
	// 	check_pwd();
	// 	check_cpwd();
	// 	check_email();
    //
	// 	if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
	// 	{
	// 		return true;
	// 	}
	// 	else
	// 	{
	// 		return false;
	// 	}
    //
	// });








})