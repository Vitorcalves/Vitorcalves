<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Formulário Exemplo 3">
        <meta name="author" content="Aldecir Fonseca">
        <title>Formulário Exemplo 3</title>

        <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>

        <?php 

        if (isset($_POST['nome'])) {
            ?>

            <div class="container">
                <h2>Formulário Exemplo 3 (result)</h2>
                <hr>

                <p>
                    <strong>Nome: </strong><?= $_POST['nome'] ?>
                </p>
                <p>
                    <strong>Telefone: </strong><?= $_POST['telefone'] ?>
                </p>
                <p>
                    <strong>E-mail: </strong><?= $_POST['email'] ?>
                </p>

                <a class="btn btn-primary btn-sm" 
                href="form-exemplo-3.php?nome=FASM&telefone=987654321&email=aldecir.fonseca2@santamarcelina.gov.br">Voltar</a>
                
            </div>

            <?php
        } else {
            return header("Location: form-exemplo-3.php?msg=Você tentou acessar o resultado sem preencher o formulário, favor preencher o formulário.");
            exit;
        }
        ?>

    </body>
</html>
