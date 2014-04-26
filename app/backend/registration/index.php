<?php
	require 'login.php'
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"></head>
	<title> Learning to Program </title>
	<link rel="stylesheet" type="text/css" href="css/global.css"></link>
	<link rel="stylesheet" type="text/css" href="css/index.css"></link>
</head>
<body>
	<h1>Learning to Program!</h1>
	<div id="login">
		<form method="post" action="index.php">
			<table id="formTable">
				<tr>
					<td><label for="emailText">Email:</label></td>
					<td><input name="email" type="text"/></td>
				</tr>
				<tr>
					<td><label for="passwordText">Password:</label></td>
					<td><input name="password" type="password"/></td>
				</tr>				
			</table>
			<input name="login" type="submit" value="Login"/>
			<input name="register" type="submit" value="Register"/>
		</form>
	</div>
</body>
</html>