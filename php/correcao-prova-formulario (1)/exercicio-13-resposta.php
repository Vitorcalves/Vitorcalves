<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Exercicio referente disciplina Programação Web II curso ADS, Calculadora PHP">
        <meta name="author" content="Aldecir Fonseca">
        
        <title>Calculo salário</title>
        
        <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
        
        <script src="js/jquery-3.3.1.js" type="text/javascript"></script>
        <script src="js/mascara.js" type="text/javascript"></script>

        <script src="bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
        
    </head>
    <body>
        
        <?php

            require_once "exercicio-13-funcoes.php";

            //

            if (!isset($_POST['qtdeAulas'])) {
                header("Location: exercicio-13-form.php" );
                exit;
            }

            $salarioBruto = ($_POST['qtdeAulas'] * strNumero($_POST['vlrHoraAula']));
            $descontoINSS = ($salarioBruto * 8) / 100;
            $baseIRRF = ($salarioBruto - $descontoINSS);
            $descontoIRRF = 0;

            if ($salarioBruto <= 1245) {
                $descontoIRRF = ($baseIRRF * 7.5) / 100;
            } elseif (($salarioBruto > 1245) && ($salarioBruto <= 2289.6)) {
                $descontoIRRF = ($baseIRRF * 9) / 100;
            } elseif (($salarioBruto > 2289.6) && ($salarioBruto <= 3334.4)) {
                $descontoIRRF = ($baseIRRF * 12) / 100;
            } elseif (($salarioBruto > 3334.4) && ($salarioBruto <= 6301.06)) {
                $descontoIRRF = ($baseIRRF * 14) / 100;
            } elseif ($salarioBruto > 6301.06) {
                $descontoIRRF = (6301.06 * 14) / 100;
            }

            $salarioLiquido = ($salarioBruto - ($descontoINSS + $descontoIRRF));
        ?>
        
        <header class="container-fluid">
            <h1>Calculo Salário - Resultado</h1>
        </header>
        
        <hr>
            
        <main class="container row">
            
            <section class="col-6">

                <table class="table table-bordered table-striped table-hover table-sm">
                
                    <thead class="thead-light">
                        <tr>
                            <th>Evento</th>
                            <th>Valor</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Salário Bruto</td>
                            <td class="text-end"><?= formataValor($salarioBruto) ?></td>
                        </tr>
                        <tr>
                            <td>Desconto INSS</td>
                            <td class="text-end"><?= formataValor($descontoINSS) ?></td>
                        </tr>
                        <tr>
                            <td>Desconto IRRF</td>
                            <td class="text-end"><?= formataValor($descontoIRRF) ?></td>
                        </tr>
                        <tr>
                            <td>Salário Líquido</td>
                            <td class="text-end"><?= formataValor($salarioLiquido) ?></td>
                        </tr>
                    </tbody>
                    
                </table>
                
            </section>
            
        </main>
        
        <footer class="container-fluid">
            <a href="exercicio-13-form.php" class="btn btn-info">Voltar</a>
        </footer>
        
    </body>
</html>
