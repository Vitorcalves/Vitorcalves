<?php 
    class Caneta {
        private $modelo;
        private $cor;
        private $ponta;
        private $tampada;


        public function getCor() {
            return $this->cor;
        }
        public function setCor($c) {
            $this->cor = $c;
        }

        public function getTampada() {
            return $this->tampada;
        }
        public function settampada($t) {
            $this->tampada = $t;
        }


        public function __construct($mo, $co, $po) { //metodo construtor
           $this->setModelo($mo);
           $this->setCor($co);
           $this->setPonta($po);

        //    $this->modelo = $mo;
        //    $this->cor = $co;
        //    $this->ponta = $po;           

           $this->tampar();
          
        }

        public function tampar() {
            $this->tampada = true;
        }

        public function getModelo() {
            return $this->modelo;
        }
        public function setModelo($m) {
            $this->modelo = $m;    
        }
        
        public function getPonta() {
            return $this->ponta;
        }
        public function setPonta($p) {
            $this->ponta = $p;
        }

       
        
    }
?>