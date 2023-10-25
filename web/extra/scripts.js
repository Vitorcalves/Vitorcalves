var ganhador = false;
var rodada = 0;
const alert = document.getElementById('alert');
const idForm = document.getElementById('form');
const btn = document.querySelector("#send");
let selectElement = document.getElementById('tabuleiro');
let selectedValue = selectElement.value;
console.log(selectedValue);

selectElement.addEventListener('change', function(){
    selectedValue = selectElement.value;
    console.log(selectedValue);
});



class Jogador {
    constructor(nome, jogadas, vitorias) {
        this.nome = nome;
        this.jogadas = jogadas;
        this.vitorias = vitorias;
    }
    ganhar(){
        this.vitorias++;
    }
    jogar(jogada){
        this.jogadas.push(jogada);
    }
}

//function para pegar os nomes dos jogadores
function teste() {
    const nome01 = document.querySelector("#nome01");
    const nome02 = document.querySelector("#nome02");
    console.log(nome01.value);
    console.log(nome02.value);
    if(nome01.value == "" || nome02.value == ""){
        X.nome = "X";
        O.nome = "O";
        document.getElementById('jogador1').innerText = X["nome"];
        document.getElementById('jogador2').innerText = O["nome"];
        return;
    }   
    X.nome = nome01.value;
    O.nome = nome02.value;
    document.getElementById('jogador1').innerText = X["nome"];
    document.getElementById('jogador2').innerText = O["nome"];
}

// Função para aceitar o clique do botão
function clique(botao) {
    botao = +botao;    
    // Verificar se o botão já foi clicado ou se já tem um ganhador
    console.log(botao);
    for (let i = 0; i < rodada; i++) {
        if (X.jogadas[i] == botao || O.jogadas[i] == botao || ganhador == true) {
            return;
        }
    }
    if (rodada == 0) {
        document.getElementById(botao).innerText = "X";
        X.jogar(botao);
        rodada++;
    }
    else if (rodada % 2 == 0) {
        document.getElementById(botao).innerText = "X";
        X.jogar(botao);
        rodada++;
        verificarVencedor(X);
    }
    else {
        document.getElementById(botao).innerText = "O";
        O.jogar(botao);
        rodada++;
        verificarVencedor(O);
    }
}
// Função para verificar se houve um vencedor
function verificarVencedor(jogador) {
    // Definir as possíveis combinações vencedoras
    console.log(verificarVencedor);
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
        console.log("comecei correr lista");
        if(jogador == X){
            correrLista(X.jogadas);
        }
        else{
            correrLista(O.jogadas);
        }
    }
    function correrLista(lista){
        for (let i = 0; i < comb.length; i++) {
            console.log("entrei no for corre lista");
            if (lista.includes(comb[i][0]) && lista.includes(comb[i][1]) && lista.includes(comb[i][2])) {  
                ganhador = true;
                mensagemAlerta(`O Jogador ${jogador.nome} Venceu!`);
                jogador.ganhar();
                break;
            }
            else{
                console.log("entrei no else");
            }
        }
    }
    
    // Verificar se houve empate
    if (rodada == 9 && ganhador == false) {
        // Mostrar uma mensagem de empate
        mensagemAlerta("O jogo terminou em empate!");
    }
}
// Função para reiniciar o jogo
function novaRodada(){
    rodada = 0;
    ganhador = false;
    X.jogadas = [];
    O.jogadas = [];
        document.getElementById('placar1').innerText = X.vitorias;
        document.getElementById('placar2').innerText = O.vitorias;
        alert.innerHTML = '';

    for(let i = 0; i < 9; i++){
        document.getElementById(i).innerText = "";
    }
}
function reiniciar(){
    rodada = 0;
    ganhador = false;
    X.jogadas = [];
    O.jogadas = [];
    X.vitorias = 0;
    O.vitorias = 0;
    document.getElementById('placar1').innerText = X.vitorias;
    document.getElementById('placar2').innerText = O.vitorias;
    alert.innerHTML = '';

    for(let i = 0; i < 9; i++){
        document.getElementById(i).innerText = "";
    }
}

// Função para mostrar uma mensagem de vitoria ou empate
function mensagemAlerta(message) {
    const escrever = document.createElement('div');
    escrever.innerHTML = [       
        
        '<div class="mensagem">',
        `   <div>${message}</div>`,
        '   <button class="restart" onclick="novaRodada();">Nova Rodada</button>',
        '   <button class="close" onclick="reiniciar();">Reiniciar</button>',
        '</div>'
    ].join('');
    alert.append(escrever);
}

btn.addEventListener('click', teste);
let X = new Jogador("X", [], 0);
let O = new Jogador("O", [], 0);