<?php 
    
    class Lutador{
        private $nome;
        private $nacionalidade;
        private $idade;
        private $altura;
        private $peso;
        private $categoria;
        private $vitorias;
        private $derrotas;
        private $empates;

        public function __construct($no, $na, $id, $al, $pe, $vi, $de, $em) {
            $this->setNome($no);
            $this->setNacionalidade($na);
            $this->setIdade($id);
            $this->setAltura($al);
            $this->setPeso($pe);
            $this->setVitorias($vi);
            $this->setDerrotas($de);
            $this->setEmpates($em);
        }

        public function apresentar(){
            echo "<p>------------------------------------</p>";
            echo "<p>Lutador: " . $this->getNome() . "</p>";
            echo "<p>Origem: " . $this->getNacionalidade() . "</p>";
            echo "<p>" . $this->getIdade() . " anos</p>";
            echo "<p>" . $this->getAltura() . " M de altura</p>";
            echo "<p>Pesando " . $this->getPeso() . "Kg</p>";
            echo "<p>Ganhou: " . $this->getVitorias() . "</p>";
            echo "<p>Perdeu: " . $this->getDerrotas() . "</p>";
            echo "<p>Empatou: " . $this->getEmpates() . "</p>";
        }

        public function status(){
            echo "<p>------------------------------------</p>";
            echo "<p>" . $this->getNome() . "</p>";
            echo "<p>É um peso " . $this->getCategoria() . "</p>";
            echo "<p>" . $this->getVitorias() . " vitorias </p>";
            echo "<p>" . $this->getDerrotas() . " derrotas </p>";
            echo "<p>" . $this->getEmpates() . " empates </p>";
        }

        public function ganharLuta(){
            $this->setVitorias($this->getVitorias() + 1);
        }

        public function perderLuta(){
            $this->setDerrotas($this->getDerrotas() + 1);
        }

        public function empatarLuta(){
            $this->setEmpates($this->getDerrotas() + 1);
        }

        public function getNome(){
            return $this->nome;
        }
        public function setNome($no){
            $this->nome = $no;
        }

        public function getNacionalidade(){
            return $this->nacionalidade;
        }
        public function setNacionalidade($na){
            $this->nacionalidade = $na;
        }

        public function getIdade(){
            return $this->idade;
        }
        public function setIdade($id){
            $this->idade = $id;
        }

        public function getAltura(){
            return $this->altura;
        }
        public function setAltura($al){
            $this->altura = $al;
        }

        public function getPeso(){
            return $this->peso;
        }
        public function setPeso($pe){
            $this->peso = $pe;
            $this->setCategoria();
        }

        public function getCategoria(){
            return $this->categoria;
        }
        private function setCategoria(){
            if ($this->peso < 52.2){
                $this->categoria = "Inválido";
            } elseif ($this->peso <= 70.3){
                $this->categoria = "Leve";
            } elseif ($this->peso <= 83.9){
                $this->categoria = "Médio";
            } elseif ($this->peso <= 120.2){
                $this->categoria = "Pesado";
            } else {
                $this->categoria = "Inválido";
            }
        }

        public function getVitorias(){
            return $this->vitorias;
        }
        public function setVitorias($vi){
            $this->vitorias = $vi;
        }

        public function getDerrotas(){
            return $this->derrotas;
        }
        public function setDerrotas($de){
            $this->derrotas = $de;
        }

        public function getEmpates(){
            return $this->empates;
        }
        public function setEmpates($em){
            $this->empates = $em;
        }


    }
?>