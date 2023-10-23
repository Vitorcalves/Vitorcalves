var jogadorX = [];
var jogadorO = [];
var rodada = 0;
var ganhador = false;
const idDiv = document.getElementById('alert')
// Função para aceitar o clique do botão
function clique(botao) {
    let id = +botao.id;
    console.log(id);
    // Verificar se o botão já foi clicado ou se já tem um ganhador
    for (let i = 0; i < jogadorX.length; i++) {
        if (jogadorX[i] == id || jogadorO[i] == id || ganhador == true) {
            return;
        }
    }
    if (rodada == 0) {
        document.getElementById(id).innerText = "X";
        jogadorX.push(id);
        rodada++;
    } else if (rodada % 2 == 0) {
        document.getElementById(id).innerText = "X";
        jogadorX.push(id);
        rodada++;
        verificarVencedor("X");
    } else {
        document.getElementById(id).innerText = "O";
        jogadorO.push(id);
        rodada++;
        verificarVencedor("O");
    }
}
// Função para verificar se houve um vencedor
function verificarVencedor(jogador) {
    // Definir as possíveis combinações vencedoras
    const comb = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];
    // Percorre as combinações e compara com os valores
    if (rodada >= 5){
        if(jogador == "X"){
            correrLista(jogadorX);
        }else{
            correrLista(jogadorO);
        }
    }
    function correrLista(lista){
        for (let i = 0; i < comb.length; i++) {
            if (lista.includes(comb[i][0]) && lista.includes(comb[i][1]) && lista.includes(comb[i][2])) {  
                ganhador = true;
                mensagemAlerta(`O Jogador ${jogador} Venceu!`);
                break;
            }
        }
    }
    
    // Verificar se houve empate
    if (rodada == 9 && ganhador == false) {
        // Mostrar uma mensagem de empate
        mensagemAlerta("O jogo terminou em empate!");
    }
}
// Função para mostrar uma mensagem de vitoria ou empate
function mensagemAlerta(message) {
    const escrever = document.createElement('div');
    escrever.innerHTML = [
        `<div class="mensagem">`,
        `   <div>${message}</div>`,
        '   <button class="close" onclick="window.location.reload();">Reiniciar</button>',
        '</div>'
    ].join('');
    idDiv.append(escrever);
}
