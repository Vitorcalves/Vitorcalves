<?php 
    require_once 'Lutador.php';
    class Luta{
        private $desafiado;
        private $desafiante;
        private $rounds;
        private $aprovada;

        public function marcarLuta($l1, $l2){
            if($l1->getCategoria() == $l2->getCategoria() && ($l1 != $l2)){
                $this->setAprovada(true);
                $this->setDesafiado($l1);
                $this->setDesafiante($l2);
            }else{
                $this->setAprovada(false);
                $this->setDesafiado(null);
                $this->setDesafiante(null);
            }
        }
        public function lutar(){
            if($this->aprovada){
                $this->desafiado->apresentar();
                $this->desafiante->apresentar();
                $vencedor = rand(0, 2);
                switch($vencedor){
                    case 0:// Empate
                        echo "<p>------------------------------------</p>";
                        echo "<p>Empate!<p/>";
                        $this->desafiado->ganharLuta();
                        $this->desafiante->perderLuta();
                        break;
                    case 1:// Desafiado vence
                        echo "<p>------------------------------------</p>";
                        echo "<p>" . $this->desafiado->getNome() . " venceu!";
                        $this->desafiado->ganharLuta();
                        $this->desafiante->perderLuta();
                        break;
                    case 2:// Desafiante vence
                        echo "<p>------------------------------------</p>";
                        echo "<p>" . $this->desafiante->getNome() . " venceu!";
                        $this->desafiado->perderLuta();
                        $this->desafiante->ganharLuta();
                        break;
                    
                }
            }

        }

        public function setDesafiado($d){
            $this->desafiado = $d;
        }
        public function getDesafiado(){
            return $this->desafiado;
        }

        public function setDesafiante($d){
            $this->desafiante = $d;
        }
        public function getDesafiante(){
            return $this->desafiante;
        }

        public function setRounds($d){
            $this->rounds = $d;
        }
        public function getRounds(){
            return $this->rounds;
        }

        public function setAprovada($d){
            $this->aprovada = $d;
        }
        public function getAprovada(){
            return $this->aprovada;
        }

    }
?>