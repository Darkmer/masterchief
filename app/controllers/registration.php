<?php

class Registration extends Controller{

	public function __construct(){
		parent::__construct();
	}

	public function index($request = null){

		$data['title'] = 'Registration';

		$this->view->rendertemplate('header',$data);
		$this->view->render('registration/registration',$data);
		$this->view->rendertemplate('footer',$data);
		echo "I WAS CALLED";
	}
}