<?php 
    require_once 'pessoa.php';
    class Aluno extends Pessoa{
        private $matricula;
        private $curso;
        
        public function pagarMensalidade(){
            echo "<p>Pagando mensalidade do aluno $this->nome";
        }

        public function setMatricula($m) {
            $this->matricula = $m;
        }
        public function getMatricula(){
            return $this->matricula;
        }

        public function setCurso($c) {
            $this->curso = $c;
        }
        public function getCurso(){
            return $this->curso;
        }
    }
?>