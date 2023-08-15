<?php 
    require_once 'aluno.php';
    class bolsista extends Aluno{
        private $bolsa;

        public function renovarBolsa(){
            echo "<p>Renovar bolsa</p>";
        }

        public function pagarMensalidade()
        {
            echo "<p>$this->nome é bolsista! então paga com desconto";
        }

        public function getBolsa(){
            return $this->bolsa;
        }
        public function setBolsa($b){
            $this->bolsa = $b;
        }
    }
?>