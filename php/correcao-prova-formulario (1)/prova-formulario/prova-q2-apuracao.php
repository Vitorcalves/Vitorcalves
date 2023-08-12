<?php

require_once "../exercicio-13-funcoes.php";

?>

<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Exercicio referente disciplina Programação Web II curso ADS, Eleições">
        <meta name="author" content="Aldecir Fonseca">
        
        <title>Apuração das Eleições</title>
        
        <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
        
        <script src="../bootstrap/js/jquery-3.3.1.js" type="text/javascript"></script>
        <script src="../bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
        
    </head>
    <body>

        <header class="container-fluid">
            <h1>Apuração das Eleições</h1>
        </header>
        
        <hr>
            
        <main class="container row">
            
            <section class="col-12">

                <table class="table table-bordered table-hover table-striped table-sm">
                    
                    <thead class="thead-light">
                        <tr>
                            <th>Candidto</th>
                            <th class="text-center">Nº de votos</th>
                            <th class="text-center">% de votos</th>
                        </tr>
                    </thead>
                    
                    <tbody>
                        <tr>
                            <td>Candidato 1</td>
                            <td class="text-center"><?= $_POST['totCandidato1'] ?></td>
                            <td class="text-center"><?= formataValor(($_POST['totCandidato1'] / $_POST['totVotos']) * 100) ?></td>
                        </tr>
                        <tr>
                            <td>Candidato 2</td>
                            <td class="text-center"><?= $_POST['totCandidato2'] ?></td>
                            <td class="text-center"><?= formataValor(($_POST['totCandidato2'] / $_POST['totVotos']) * 100) ?></td>
                        </tr>
                        <tr>
                            <td>Candidato 3</td>
                            <td class="text-center"><?= $_POST['totCandidato3'] ?></td>
                            <td class="text-center"><?= formataValor(($_POST['totCandidato3'] / $_POST['totVotos']) * 100) ?></td>
                        </tr>
                        <tr>
                            <td>Branco</td>
                            <td class="text-center"><?= $_POST['totBranco'] ?></td>
                            <td class="text-center"><?= formataValor(($_POST['totBranco'] / $_POST['totVotos']) * 100) ?></td>
                        </tr>
                        <tr>
                            <td>Nulo</td>
                            <td class="text-center"><?= $_POST['totNulo'] ?></td>
                            <td class="text-center"><?= formataValor(($_POST['totNulo'] / $_POST['totVotos']) * 100) ?></td>
                        </tr>
                    </tbody>
                    
                </table>
                
            </section>
            
        </main>
        
        <footer class="container-fluid"> 
            <a href="prova-q2-form.php" class="btn btn-info btn-sm">Voltar</a>
        </footer>
        
    </body>
</html>
