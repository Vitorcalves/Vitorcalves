<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
        require_once 'pessoas.php';
        require_once 'aluno.php';
        require_once 'professor.php';
        require_once 'funcionario.php';

        $p1 = new pessoa();
        $p2 = new aluno();
        $p3 = new professor();
        $p4 = new funcionario();

        $p1->setNome("Pedro");
        $p2->setNome("Maria");
        $p3->setNome("Cláudio");
        $p4->setNome("Fabiana");

        $p2->setCurso("Informatica");
        $p3->setSalario(2500.75);
        $p4->setSetor("Estoque");

        $p1->setSexo("M");
        $p4->setSexo("F");

        $p3->ReceberAum(550.20);
        $p4->mudarTrabalho();
        $p2->cancelarMatr();

        print_r($p1);
        echo "<br>";
        print_r($p2);
        echo "<br>";
        print_r($p3);
        echo "<br>";
        print_r($p4);
        echo "<br>";


    ?>
</body>
</html>