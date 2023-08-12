<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Exercicio referente disciplina Programação Web II curso ADS, Eleições">
        <meta name="author" content="Aldecir Fonseca">
        
        <title>Eleições</title>
        
        <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
        
        <script src="../bootstrap/js/jquery-3.3.1.js" type="text/javascript"></script>
        <script src="../bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
        
    </head>
    <body>

        <?php

            $totCandidato1  = 0;
            $totCandidato2  = 0;
            $totCandidato3  = 0;
            $totBranco      = 0;
            $totNulo        = 0;
            $totVotos       = 0;

            if (isset($_POST['voto'])) {

                $totCandidato1  = (int)$_POST['totCandidato1'];
                $totCandidato2  = (int)$_POST['totCandidato2'];
                $totCandidato3  = (int)$_POST['totCandidato3'];
                $totBranco      = (int)$_POST['totBranco'];
                $totNulo        = (int)$_POST['totNulo'];

                switch ($_POST['voto']) {
                    case 1:
                        $totCandidato1++;
                        break;
                    case 2:
                        $totCandidato2++;
                        break;
                    case 3:
                        $totCandidato3++;
                        break;
                    case 4:
                        $totBranco++;
                        break;
                    case 5:
                        $totNulo++;
                        break;
                }

                $totVotos       = ($totCandidato1 + $totCandidato2 + $totCandidato3 + $totBranco + $totNulo);   
            }

        ?>

        <header class="container-fluid">
            <h1>Eleições</h1>
        </header>
        
        <hr>
            
        <main class="container row">
            
            <section class="col-12">
                
                <form method="POST" action="prova-q2-form.php">

                    <input type="hidden" name='totCandidato1' id='totCandidato1' value="<?= $totCandidato1 ?>">
                    <input type="hidden" name='totCandidato2' id='totCandidato2' value="<?= $totCandidato2 ?>">
                    <input type="hidden" name='totCandidato3' id='totCandidato3' value="<?= $totCandidato3 ?>">
                    <input type="hidden" name='totBranco'     id='totBranco'     value="<?= $totBranco ?>">
                    <input type="hidden" name='totNulo'       id='totNulo'       value="<?= $totNulo ?>">
                    
                    <div class="form-check">
                        <input type="radio" class="form-check-input" name="voto" id="voto1" value="1">
                        <label class="form-check-label" for="voto1">
                            Candidato 1
                        </label>
                    </div>                   

                    <div class="form-check">
                        <input type="radio" class="form-check-input" name="voto" id="voto2" value="2">
                        <label class="form-check-label" for="voto2">
                            Candidato 2
                        </label>
                    </div>                   

                    <div class="form-check">
                        <input type="radio" class="form-check-input" name="voto" id="voto3" value="3">
                        <label class="form-check-label" for="voto3">
                            Candidato 3
                        </label>
                    </div>                   

                    <div class="form-check">
                        <input type="radio" class="form-check-input" name="voto" id="voto4" value="4">
                        <label class="form-check-label" for="voto4">
                            Branco
                        </label>
                    </div>                   

                    <div class="form-check">
                        <input type="radio" class="form-check-input" name="voto" id="voto5" value="5">
                        <label class="form-check-label" for="voto5">
                            Nulo
                        </label>
                    </div>                   

                    <div class="form-group row">
                        <div class="col-12">
                            <button type="submit" class="btn btn-success btn-sm"
                                <?= ($totVotos > 10 ? "disabled" : "") ?>>
                                Confirmar Voto
                            </button>
                        </div>
                    </div>

                </form> 
                
                <form method="POST" action="prova-q2-apuracao.php">

                    <input type="hidden" name='totCandidato1' id='totCandidato1' value="<?= $totCandidato1 ?>">
                    <input type="hidden" name='totCandidato2' id='totCandidato2' value="<?= $totCandidato2 ?>">
                    <input type="hidden" name='totCandidato3' id='totCandidato3' value="<?= $totCandidato3 ?>">
                    <input type="hidden" name='totBranco'     id='totBranco'     value="<?= $totBranco ?>">
                    <input type="hidden" name='totNulo'       id='totNulo'       value="<?= $totNulo ?>">
                    <input type="hidden" name='totVotos'      id='totVotos'      value="<?= $totVotos ?>">
                    
                    <div class="form-group row mt-3">
                        <div class="col-12">
                            <button type="submit" class="btn btn-danger btn-sm" <?= ($totVotos >= 6 ? "" : "disabled") ?>>
                                Apurar Eleição
                            </button>
                        </div>
                    </div>
                </form>
                
            </section>
            
        </main>

    </body>
    
</html>