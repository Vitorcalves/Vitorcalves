<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Exercicio referente disciplina Programação Web II curso ADS">
        <meta name="author" content="Aldecir Fonseca">
        
        <title>Login</title>
        
        <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
        
        <script src="js/jquery-3.3.1.js" type="text/javascript"></script>
        <script src="bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
        
    </head>
    <body>
        
        <?php
            $logado = false;
            $msgError = "";
            $tentativasLogin = 0;

            if (isset($_POST['login'])) { 
                $tentativasLogin = ($_POST['tentativasLogin'] + 1); 
                
                if ($tentativasLogin > 3) {
                    $msgError = "Número de tentativas excedido, favor tentar mais tarde";
                } else {

                    if ($_POST['login'] == "fasm") { // verifica o login informado
                        if ($_POST['senha'] == "fasm3p2023") { // verifica a senha
                            $logado = true;
                        } else {
                            $msgError = "Senha incorreta.";
                        }
                    } else {
                        $msgError = "Usuário incorreto.";
                    }

                }
            }
        ?>

        <header class="container-fluid">
            <h1>Login</h1>
        </header>
        
        <hr>
        
        <main class="container row">

            <section class="col-12 col-sm-8 col-md-4">

                <?php if (!$logado): ?>

                    <form method="POST" action="exercicio-12-form.php">

                        <input type="hidden" name="tentativasLogin" value="<?= $tentativasLogin ?>">
                
                        <div class="form-group row">
                            <label for="login" class="col-sm-6 col-md-4 col-form-label">Login</label>
                            <div class="col-sm-6 col-md-8">
                                <input type="text" class="form-control" name="login" id="login"
                                    required=""
                                    autofocus=""
                                    value="<?= (isset($_POST['login']) ? $_POST['login'] : "") ?>">
                            </div>
                        </div>
                        <div class="form-group row mt-3">
                            <label for="senha" class="col-sm-6 col-md-4 col-form-label">Senha</label>
                            <div class="col-sm-6 col-md-8">
                                <input type="password" class="form-control" name="senha" id="senha"
                                    required="">
                            </div>
                        </div>

                        <?php 
                            if (!empty($msgError)) {
                                ?>
                                <div class="form-group row mt-3">
                                    <div class="offset-4 col-8">
                                        <div class="alert alert-danger alert-dismissible fade show" role="alert">
                                            <?= $msgError ?>
                                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                        </div>
                                    </div>
                                </div>
                                <?php
                            }
                        ?>

                        <div class="form-group row mt-3">
                            <div class="col-sm-6 col-md-4 col-form-label"></div>
                            <div class="col-sm-6 col-md-8">
                                <button type="submit" <?= ($tentativasLogin > 3 ? 'disabled' : "") ?> class="btn btn-primary btn-sm">Entrar</button>
                            </div>
                        </div>

                    </form>
                
                <?php else: ?>

                    <div class="alert alert-success" role="alert">
                        Meus parabéns! Você acessou nosso sistema.
                    </div>  

                    <div class="mb-3 row">
                        <div class="col-sm-10">
                            <a href="exercicio-12-form.php" class="btn btn-secondary btn-sm">Voltar</a>
                        </div>
                    </div>

                <?php endif; ?>

            </section>

        </main>

    </body>
    
</html>