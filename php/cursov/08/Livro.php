<?php 
    require_once "Pessoa.php";
    require_once "Publicacao.php";
    class Livro implements Publicacao{
        private $titulo;
        private $autor;
        private $totPagina;
        private $pagAtual;
        private $aberto;
        private $leitor;

        public function __construct($ti, $au, $to) {
            $this->setTitulo($ti);
            $this->setAutor($au);
            $this->setTotPagina($to);
            $this->setPagAtual(0);
            $this->setAberto(false);
        }

        function detalhes() {
            echo "<p>-----------------------------------</p>";
            echo "<p>O livro " . $this->getTitulo() . "</p>";
            echo "<p>Do autor " . $this->getAutor() . "</p>";
            echo "<p>Com " . $this->getTotPagina() . " paginas no total";
        }

        public function abrir(){
            $this->setAberto(true);
        }

        public function fechar(){
            $this->setAberto(false);
        }

        public function folhear($fo){
            $this->setPagAtual($fo);
        }

        public function avancarPag(){
            $this->setPagAtual($this->getPagAtual() + 1);
        }

        public function voltarPag(){
            $this->setPagAtual($this->getPagAtual() - 1);
        }


        public function getTitulo(){
            return $this->titulo;
        }
        public function setTitulo($t){
            $this->titulo = $t;
        }

        public function getAutor(){
            return $this->autor;
        }
        public function setAutor($a){
            $this->autor = $a;
        }

        public function getTotPagina(){
            return $this->totPagina;
        }
        public function setTotPagina($tp){
            $this->totPagina = $tp;
        }

        public function getPagAtual(){
            return $this->pagAtual;
        }
        public function setPagAtual($pa){
            $this->pagAtual = $pa;
        }

        public function getAberto(){
            return $this->aberto;
        }
        public function setAberto($ab){
            $this->aberto = $ab;
        }

        public function getLeitor(){
            return $this->leitor;
        }
        public function setLeitor($l){
            $this->leitor = $l;
        }


    }
?>