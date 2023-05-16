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
        <script src="js/jqueryMask.js" type="text/javascript"></script>
        
        <script src="bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
        
    </head>
    <body>
        
        <header class="container-fluid">
            <h1>Calculo Salário</h1>
        </header>
        
        <hr>
        
        <main class="container row">
            
            <section class="col-6">
                
                <form method="POST" action="exercicio-13-resposta.php">

                    <div class="form-group row mt-2">
                        <label for="qtdeAulas" class="col-sm-6 col-md-6 col-form-label">Quantidade de Aulas dadas</label>
                        <div class="col-sm-6 col-md-6">
                            <input type="number" class="form-control" name="qtdeAulas" id="qtdeAulas"
                                min="1" max="200"
                                required=""
                                autofocus="">
                        </div>
                    </div>
                    <div class="form-group row mt-2">
                        <label for="vlrHoraAula" class="col-sm-6 col-md-6 col-form-label">Valor da hora Aula</label>
                        <div class="col-sm-6 col-md-6">
                            <input type="text" class="form-control" name="vlrHoraAula" id="vlrHoraAula"
                                dir="rtl"
                                required="">
                        </div>
                    </div>
                            
                    <div class="form-group row mt-2">
                        <div class="col-sm-6 col-md-6 col-form-label"></div>
                        <div class="col-sm-6 col-md-6">
                            <button type="submit" class="btn btn-primary btn-sm">Calcular</button>
                        </div>
                    </div>

                </form> 

            </section>
            
        </main>

    </body>
    
</html>
