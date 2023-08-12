
SELECT j.cod, j.nome, g.genero, p.produtora, j.descricao, j.nota, j.capa FROM jogos j
JOIN generos g ON j.genero = g.cod JOIN produtora p ON j.produtora - p.cod;