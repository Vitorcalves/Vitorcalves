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

            function formataValor($valor, $decimais = 2)
            {
                return number_format($valor, $decimais, ",", ".");
            }

            function strNumero($valor)
            {
                return str_replace(",", ".", str_replace(".", "", $valor));
            }

            /*
            include: 
            “Include” irá adicionar o arquivo especificado na execução 
            do script, e caso não seja encontrado, irá retornar um erro do 
            tipo “warning” com mensagem de “arquivo não encontrado”.
            
            include_once:   
            A mesma função do “include” simples, mas não irá incluir 
            o arquivo novamente, caso já tenha sido adicionado anteriormente 
            na execução.
            
            require:    
            Basicamente irá realizar a mesma função que os includes, 
            mas como o próprio nome descreve, o script requer o arquivo 
            para continuar a execução. Sem esse “require”, o script 
            será parado de executar e retornará um “fatal error”, ou seja, 
            irá parar de executar o script.

            require_once: 
            Mesma funcionalidade do “require”, mas com o “once” 
            junto, só irá incluir o arquivo se não houver uma chamada 
            anterior do mesmo.             
            
            */

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
