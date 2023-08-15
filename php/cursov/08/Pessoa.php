<?php 
    class Pessoa{
        private $nome;
        private $idade;
        private $sexo;

        public function __construct($n, $i, $s) {
            $this->nome = $n;
            $this->idade = $i;
            $this->sexo = $s;
        }

        public function fazerAniversario(){
            $this->setIdade($this->getIdade() + 1);
        }

        public function setNome($no){
            $this->nome = $no;
        }
        public function getNome(){
            return $this->nome;
        }

        public function setIdade($id){
            $this->idade = $id;
        }
        public function getIdade(){
            return $this->idade;
        }

        public function setSexo($se){
            $this->sexo = $se;
        }
        public function getSexo(){
            return $this->sexo;
        }
    }
?>