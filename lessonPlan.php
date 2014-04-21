<?php
	require 'login.php';
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"></head>
	<title> Learning to Program </title>
	<link rel="stylesheet" type="text/css" href="resources/global.css"></link>
	<link rel="stylesheet" type="text/css" href="resources/lessonPlan.css"></link>
	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
	<link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/themes/smoothness/jquery-ui.css" />
	<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
	<script>
		  $(function() {
		    $( "#accordion" ).accordion();
		  });
  	</script>
</head>
<body>
	<div id="wrapper">
		<h1>Learning to Program!</h1>
		<h2><?php echo $_SESSION['firstName']?>'s Lesson Plan</h2>
		<div id="accordion">
			<h3>Lesson 1</h3>
			<div>Lesson 1 Content</div>
			<h3>Lesson 2</h3>
			<div>Lesson 2 Content</div>
			<h3>Lesson 3</h3>
			<div>Lesson 3 Content</div>
			<h3>Lesson 4</h3>
			<div>Lesson 4 Content</div>
		</div>
	</div>
</body>
</html>

