<?php
//IComponent.php
interface IComponent
{
    public function operation();
    public function add(IComponent $child);
    public function remove(IComponent $cchild);
    public function getChild($someInt);
    public function getLevel();

}

interface IResponsibility
{
    public function handle($request);
    public function setSuccessor($someInt);
    public function setPredecessor($someInt);
    public function getPredecessor($someInt);
    public function getSuccessor($someInt);
}

//Composite.php
class Composite implements IComponent
{
    private $sName;
    private $aChildren;
 
    public function __construct($sNodeName)
    {
        $this->sName=$sNodeName;
        $this->aChildren=array();
    }
 
    public function add(IComponent $child)
    {
        array_push($this->aChildren,$child);
    }
 
    public function remove(IComponent $child)
    {
        //Code to remove component
    }
 
    public function getChild($someInt)
    {
        //Code to get child by element value
    }
 
    public function getlevel()
    {
        //Code to remove component
    }

    //Note: The following method is recursive
    public function operation()
    {
        echo $this->sName . "<br />";
        foreach($this->aChildren as $elVal)
        {
            $elVal->operation();
        }
    }
}

class Leaf implements IComponent
{
    private $sName;
 
    public function __construct($sNodeName)
    {
        $this->sName=$sNodeName;
    }
 
    /* None of this batch of methods are used by Leaf */
    /* However in order to correctly implement the interface */
    /* you need some kind of implementation */
    public function add(IComponent $child){}
    public function remove(IComponent $child){}
    public function getChild($someInt){}
    public function getlevel(){}
 
    /* Some userful content is required for the operation */
    public function operation()
    {
        echo $this->sName . "<br />";
    }
}

class Client
{
    private $rootCompos;
 
    public function __construct()
    {
        $this->rootCompos = new Composite("Root");
        $n1=new Composite("-Composite 1");
        $n1->add(new Leaf("--C1:leaf 1"));
        $n1->add(new Leaf("--C1:leaf 2"));
        $this->rootCompos->add($n1);
 
        $n2=new Composite("-Composite 2");
        $n2->add(new Leaf("--C2:leaf 3"));
        $n2->add(new Leaf("--C2:leaf 4"));
        $n2->add(new Leaf("--C2:leaf 5"));
        $this->rootCompos->add($n2);
 
        $this->rootCompos->add(new Leaf("R:leaf 6"));
 
        //Create a node
        $this->rootCompos->operation();
    }
}
$worker=new Client();

?>