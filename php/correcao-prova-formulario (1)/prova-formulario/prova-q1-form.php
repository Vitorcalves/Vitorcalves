<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Exercicio referente disciplina Programação Web II curso ADS, Eleições">
        <meta name="author" content="Aldecir Fonseca">
        
        <title>Formulário de Inscrição</title>
        
        <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
        
        <script src="../bootstrap/js/jquery-3.3.1.js" type="text/javascript"></script>
        <script src="../bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
        
    </head>
    <body>

        <header class="container-fluid">
            <h1>Formulário de Inscrição</h1>
        </header>
        
        <hr>
        
        <main class="container">

            <div class="row">

                <section class="col-12">
                    
                    <form method="POST" action="prova-q1-resultado.php">
                        
                        <div class="mb-3">
                            <label class="form-label" for="nome">Nome</label>
                            <input type="text" class="form-control" name="nome" id="nome" required autofocus>
                        </div>

                        <div class="mb-3">
                            <label class="form-label" for="email">E-mail</label>
                            <input type="email" class="form-control" name="email" id="email" required>
                        </div>

                        <div class="mb-3">
                            <label class="form-label" for="telefone">Telefone</label>
                            <input type="text" class="form-control" name="telefone" id="telefone" required maxlength="15">
                        </div>

                        <div class="mb-3">
                            <label class="form-label" for="dataNascimento">Data de Nascimento</label>
                            <input type="date" class="form-control" name="dataNascimento" id="dataNascimento" required>
                        </div>

                        <div class="mb-3">
                            <label class="form-label" for="cidade">Cidade</label>
                            <input type="text" class="form-control" name="cidade" id="cidade" required maxlength="50">
                        </div>

                        <button type="submit" class="btn btn-success btn-sm">Confirmar</button>

                    </form> 
                    
                </section>

            </div>
            
        </main>

    </body>
    
</html>