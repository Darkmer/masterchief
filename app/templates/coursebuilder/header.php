<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> 
<html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title><?php echo $data['title'].' - '.SITETITLE; //SITETITLE defined in index.php?></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="<?php echo url::get_template_path();?>css/bootstrap.min.css">
        <style>
            body {
                padding-top: 50px;
                padding-bottom: 20px;
            }
        </style>
        <link rel="stylesheet" href="<?php echo url::get_template_path();?>css/bootstrap.spacelab.css">
        <link rel="stylesheet" href="<?php echo url::get_template_path();?>css/main.css">

        <script src="<?php echo url::get_template_path();?>js/vendor/modernizr-2.6.2-respond-1.1.0.min.js"></script>
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
	    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
	      <div class="container">
	        <div class="navbar-header">
	          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
	            <span class="sr-only">Toggle navigation</span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	          </button>
	          <a class="navbar-brand" href="<?php echo url::get_root();?>">Rensselaer Course Builder</a>
	        </div>
	        <div class="navbar-collapse collapse">
	          <ul class="nav navbar-nav navbar-left"> 
				<li><a href="<?php echo url::get_root();?>authentication" role="button">Registration Test</a></li>
	          </ul>
			  <ul class="nav navbar-nav navbar-right">   

		        <li class="dropdown">
		          <a class="dropdown-toggle" role="button" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-user"></i> Admin <span class="caret"></span></a>
		          <ul id="g-account-menu" class="dropdown-menu" role="menu">
		            <li><a href="#">My Profile</a></li>
		            <li><a href="#">Course Management</a></li>
		          </ul>
		        </li>
		        <li><a href="#"><i class="glyphicon glyphicon-lock"></i> Logout</a></li>
		      </ul>
	        </div><!--/.navbar-collapse -->
	      </div>
	    </div>