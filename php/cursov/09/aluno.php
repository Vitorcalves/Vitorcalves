<?php
require_once 'pessoas.php';
class aluno extends pessoa
{
    private $matr;
    private $curso;

    public function cancelarMatr()
    {
        echo "<p>Matricula sera cancelada</p>";
    }

    public function getMatr()
    {
        return $this->matr;
    }
    public function setMatr($m)
    {
        $this->matr = $m;
    }

    public function getCurso()
    {
        return $this->curso;
    }
    public function setCurso($c)
    {
        $this->curso = $c;
    }

}
?>