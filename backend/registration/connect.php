<?php

$config = array(
		'DB_HOST'	=> 'localhost',
		'DB_USERNAME' => 'root',
		'DB_PASSWORD' => '');

try
{
	$conn = new PDO('mysql:host=' . $config['DB_HOST'] . ';dbname=softwaredevproject',
					$config['DB_USERNAME'], $config['DB_PASSWORD']);	
}
catch(PDOException $e)
{
	echo 'ERROR: ' . $e->getMessage();
}

?>