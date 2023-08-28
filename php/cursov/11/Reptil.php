<?php 
    require_once "Animal.php";
    class Reptil extends Animal{

        private $corEscama; 

        public function locomover()
        {
            echo "rastejando";
        }
        public function alimentar()
        {
            echo "comendo vegetais";
        }
        public function emitirSom()
        {
            echo "som de reptil";
        }

        public function getCorEscama(){
            return $this->corEscama;
        }
        public function setCorEscama($e){
            $this->corEscama = $e;
        }
}
?>