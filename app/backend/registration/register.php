<?php
	session_start();

	//Connect to the database
	require 'connect.php';

	if(isset($_POST['register']) && $_POST['register'] == 'Register')  
	{
		//Check that all form fields have been filled in
		if(!isset($_POST['email']) || !isset($_POST['passwordText']) || !isset($_POST['confirmPasswordText']) || !isset($_POST['firstName']) || !isset($_POST['lastName']) || !isset($_POST['birthday']) || !isset($_POST['city']) || !isset($_POST['state']))
		{
			echo 'Please fill in all form fields';
		}
		//Make sure passwords match each other
		else if($_POST['passwordText'] !== $_POST['confirmPasswordText'])
		{
			echo 'Passwords must match';
		}

		//Check for duplicate email address
		$stmt = $conn->prepare("SELECT COUNT(*) FROM users WHERE email=:email");
		$stmt->execute(array(':email' => $_POST['email']));
		$result = $stmt->fetch();

		if($result['COUNT(*)'] > 0)
		{
			echo 'Email already exists';
		}
		else //Add to database!
		{
			//Generate salt
			$salt = hash('sha256', uniqid(mt_rand(), true));

			//Apply salt before hashing
			$salted = hash('sha256', $salt . $_POST['passwordText']);

			$stmt = $conn ->prepare(
				"INSERT INTO users(email, password, salt, is_admin, firstName, lastName, joinDate, birthday, city, state)
				VALUES (:email, :password, :salt, :is_admin, :firstName, :lastName, CURDATE(), :birthday, :city, :state)
				");
			$stmt->execute(array(
				':email' => $_POST['email'],
				':password' => $salted,
				':salt' => $salt,
				':is_admin' => 0,
				':firstName' => $_POST['firstName'],
				':lastName' => $_POST['lastName'],				
				':birthday' => $_POST['birthday'],
				':city' => $_POST['city'],
				':state' => $_POST['state']));

			$_SESSION['email'] = $user['email'];		
			$_SESSION['firstName'] = $user['firstName'];	

			//Account successfully created
			header('Location: lessonPlan.php');
		}
	}
?>