<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
        require_once 'Caneta.php';
        $c1 = new Caneta("BIC", "Azul", 0.5);
        // $c1->setModelo("BIC");
        // // $c1->setPonta(0.5);
        print "eu tenho uma caneta {$c1->getModelo()} de ponta {$c1->getPonta()} da cor {$c1->getCor()}";
      

    ?>
</body>
</html>