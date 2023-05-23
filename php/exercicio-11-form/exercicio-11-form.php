<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício 11</title>

    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css">

</head>
<body>

    <header>
        <h3>Resolução exercício 11</h3>
    </header>

    <hr>

    <main class="container row">

        <?php

            $aCartao = [
                "1" => "América Express",
                "2" => "Discover Network",
                "3" => "Elo",
                "4" => "Master",
                "5" => "Visa",
                "6" => "Nunbak"
            ];

        ?>

        <?php if (!isset($_GET['nome'])): ?>

            <form>

                <div class="mb-3 row">
                    <label for="nome" class="col-sm-2 col-form-label">Nome</label>
                        <div class="col-sm-10">
                        <input type="text" class="form-control" id="nome" name="nome" required autofocus>
                    </div>
                </div>

                <div class="mb-3 row">
                    <label for="email" class="col-sm-2 col-form-label">E-mail</label>
                        <div class="col-sm-10">
                        <input type="email" class="form-control" id="email" name="email" placeholder="email@example.com" required>
                    </div>
                </div>

                <div class="mb-3 row">
                    <label for="dataNascimento" class="col-sm-2 col-form-label">Data Nascimento</label>
                        <div class="col-sm-10">
                        <input type="date" class="form-control" id="dataNascimento" name="dataNascimento" required>
                    </div>
                </div>

                <div class="mb-3 row">
                    <label for="bandeiraCartao" class="col-sm-2 col-form-label">Cartão de Crédito</label>
                    <div class="col-sm-10">
                        <select class="form-select" name="bandeiraCartao" id="bandeiraCartao" required>
                            <option selected>Selecione uma bandeira</option>
                            <?php foreach ($aCartao as $key => $value): ?>
                                <option value="<?= $key ?>"><?= $value ?></option>
                            <?php endforeach; ?>
                        </select>            
                    </div>
                </div>

                <button type="submit" class="btn btn-secondary btn-lg">Enviar</button>
                
            </form>

        <?php else: ?>

            <section>
                <h2>Resultado do envio do formulário</h2>
                <div class="mb-3 row">
                    <label for="nome" class="col-sm-2 col-form-label">Nome</label>
                    <div class="col-sm-10">
                        <?= $_GET['nome'] ?>
                    </div>
                </div>

                <div class="mb-3 row">
                    <label for="email" class="col-sm-2 col-form-label">E-mail</label>
                    <div class="col-sm-10">
                        <?= $_GET['email'] ?>
                    </div>
                </div>

                <div class="mb-3 row">
                    <label for="dataNascimento" class="col-sm-2 col-form-label">Data Nascimento</label>
                    <div class="col-sm-10">
                        <?= date("d/m/Y", strtotime($_GET['dataNascimento'])) ?>
                    </div>
                </div>

                <div class="mb-3 row">
                    <label for="bandeiraCartao" class="col-sm-2 col-form-label">Cartão de Crédito</label>
                    <div class="col-sm-10">
                        <?= $_GET['bandeiraCartao'] . " - " . $aCartao[$_GET['bandeiraCartao']] ?>
                    </div>
                </div>

                <div class="mb-3 row">
                    <div class="col-sm-10">
                        <a href="exercicio-11-form.php" class="btn btn-secondary btn-sm">Voltar</a>
                    </div>
                </div>
            </section>

            <?php
                date_default_timezone_set('America/Sao_Paulo');

                echo "data atual: " . date('d/m/Y');
                echo "<br> hora atual: ". date('H:i:s');
            ?>

        <?php endif; ?>

    </main>

    <footer>

    </footer>

</body>
</html>