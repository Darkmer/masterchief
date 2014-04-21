<?php
	session_start();

	//Connect to the database
	require 'connect.php';

	if(isset($_POST['login']) && $_POST['login'] == 'Login')  //Make sure the 'name' attribute of the login button = "login" and the value = 'Login'
	{
		$salt_stmt = $conn->prepare('SELECT salt FROM users WHERE email=:email');
		$salt_stmt->execute(array(':email' => $_POST['email']));
		$result = $salt_stmt->fetch();
		$salt = ($result) ? $result['salt'] : '';
		$salted = hash('sha256', $salt . $_POST['password']);

		$login_stmt = $conn->prepare('SELECT email, firstName FROM users WHERE email=:email AND password=:password');
		$login_stmt->execute(array(':email' => $_POST['email'], ':password' => $salted));

		if($user = $login_stmt->fetch())
		{
			$_SESSION['email'] = $user['email'];		
			$_SESSION['firstName'] = $user['firstName'];	
			header('Location: lessonPlan.php');
		}
		else
		{
			echo 'Incorrect email or password';
		}
	}

	if(isset($_POST['register']) && $_POST['register'] == 'Register')
	{
		header('Location: register.html');
	}
?>