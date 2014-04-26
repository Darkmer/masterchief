<?php 
class Model { 
    public $text; 
     
    public function __construct() { 
        $this->text = 'Hello world!'; 
    }         
} 

class View { 
    private $model; 
    private $route; 
     
    public function __construct($route, Model $model) { 
        $this->route = $route; 
        $this->model = $model; 
    } 
     
    public function output() { 
        return '<a href="index.php?route=' . $this->route . '&action=textclicked">' . $this->model->text . '</a>'; 
    }     
} 
  
class Controller { 
    private $model; 

    public function getName() { 
        return 'Controller'; //In the real world this may well be get_class($this), and this method defined in a parent class. 
    } 
     
    public function __construct(Model $model) { 
        $this->model = $model; 
    } 

    public function textClicked() { 
        $this->model->text = 'Text Updated'; 
    } 
} 

class Route { 
    public $model; 
    public $view; 
    public $controller; 
     
    public function __construct($model, $view, $controller) { 
        $this->model = $model; 
        $this->view = $view; 
        $this->controller = $controller;         
    } 
} 
  
class Router { 
    private $table = array(); 
     
    public function __construct() { 
        $this->table['controller'] = new Route('Model', 'View', 'Controller');
        $this->table['login'] = new Route('Model', 'index.html', 'Controller')
    } 
     
    public function getRoute($route) { 
        $route = strtolower($route); 

        //Return a default route if no route is found 
        if (!isset($this->table[$route])) { 
            return $this->table['controller'];     
        } 
         
        return $this->table[$route];         
    } 
} 

class FrontController { 
    private $controller; 
    private $view; 
     
    public function __construct(Router $router, $routeName, $action = null) { 
        $route = $router->getRoute($routeName); 
        $modelName = $route->model; 
        $controllerName = $route->controller; 
        $viewName = $route->view; 
         
        $model = new $modelName; 
        $this->controller = new $controllerName($model); 
        $this->view = new $viewName($routeName, $model); 
         
         
        if (!empty($action)) $this->controller->{$action}(); 
    } 
     
    public function output() { 
        //This allows for some consistent layout generation code  
        $header = '<h1>Hello world example</h1>'; 
        return $header . '<div>' . $this->view->output() . '</div>'; 
    } 
} 

$frontController = new FrontController(new Router, $_GET['route'], isset($_GET['action']) ? $_GET['action'] : null); 
echo $frontController->output();

?>