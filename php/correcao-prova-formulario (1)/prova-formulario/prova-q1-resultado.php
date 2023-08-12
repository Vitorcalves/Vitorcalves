<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Exercicio referente disciplina Programação Web II curso ADS, Eleições">
        <meta name="author" content="Aldecir Fonseca">
        
        <title>Resultado da Inscrição</title>
        
        <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
        
        <script src="../bootstrap/js/jquery-3.3.1.js" type="text/javascript"></script>
        <script src="../bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
        
    </head>
    <body>

        <header class="container-fluid">
            <h1>Resultado da Inscrição</h1>
        </header>
        
        <hr>
        
        <main class="container">

            <div class="row">
                <p>
                    Nome: <strong><?= $_POST['nome'] ?></strong>
                </p>
                <p>
                    E-mail: <strong><?= $_POST['email'] ?></strong>
                </p>
                <p>
                    Telefone: <strong><?= $_POST['telefone'] ?></strong>
                </p>
                <p>
                    Data de Nascimento: <strong><?= date("d/m/Y", strtotime($_POST['dataNascimento'])) ?></strong>
                </p>
                <?php
                    $idade = date("Y") - date("Y", strtotime($_POST['dataNascimento']));
                ?>
                <p>
                    Cidade: <strong><?= $_POST['cidade'] ?></strong>
                </p>

                <?php if ($idade < 18): ?>
                    <div class="alert alert-danger" role="alert">
                        Desculpe. Mas as inscrições somente podem ser realizada por maiores de idade.
                    </div>
                <?php else: ?>
                    <div class="alert alert-success" role="alert">
                        Meus parabéns! Sua inscrição foi realizada com sucesso!
                    </div>
                <?php endif; ?>

            </div>
            
        </main>

        <footer class="container"> 
            <a href="prova-q1-form.php" class="btn btn-info btn-sm">Voltar</a>
        </footer>

    </body>
    
</html>