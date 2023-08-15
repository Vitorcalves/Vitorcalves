<?php 
require_once 'pessoas.php';
    class professor extends pessoa{
        private $especialidade;
        private $salario;

        public function ReceberAum($valor){
            $this->setSalario($this->getSalario() + $valor);
        }

        public function getEspecialidade(){
            return $this->especialidade;
        }
        public function setEspecialidade($e){
            $this->especialidade = $e;
        }

        public function getSalario(){
            return $this->salario;
        }
        public function setSalario($s){
            $this->salario = $s;
        }
    }
?>