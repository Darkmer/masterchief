<?php
require('app/core/autoloader.php');

//define routes
Router::get('/', 'welcome@index');
Router::get('/authentication', 'registration@index');

//if no route found
Router::error('error@index');

//execute matched routes
Router::dispatch();
ob_flush();
