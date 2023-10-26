var ganhador = false;
var rodada = 0;
const alert = document.getElementById('alert');
const idForm = document.getElementById('form');
const idTabuleiro = document.getElementById('tabuleiro');
const btn = document.querySelector("#send");
let selectElement = document.getElementById('tamanhoJogo');
let selectedValue = selectElement.value;
criarTabuleiro();
console.log(selectedValue);

selectElement.addEventListener('change', function(){
    selectedValue = selectElement.value;
    // idTabuleiro.innerHTML = "";
    rodada = 0;
    ganhador = false;
    criarTabuleiro();
    console.log(selectedValue);
});
function criarTabuleiro() {
    idTabuleiro.innerHTML = '';
    let tabela = document.createElement('table');
    tabela.className = "game";
    tabela.id = "tabuleiro";
    idTabuleiro.appendChild(tabela);
    let contador = 0;
    for(let i = 0; i < selectedValue; i++){
        let linha = document.createElement('tr');
        tabela.appendChild(linha);
        for(let j = 0; j < selectedValue; j++){
            let celula = document.createElement('td');
            linha.appendChild(celula);
            let botao = document.createElement('button');
            botao.className = "campo";
            botao.id = i + '-' + j;
            botao.setAttribute('onclick', `clique(this.id)`);
            celula.appendChild(botao);
        }
    }
}


btn.addEventListener('click', teste);


class Jogador {
    constructor(nome, vitorias) {
        this.nome = nome;
        this.vitorias = vitorias;
    }
    ganhar(){
        this.vitorias++;
    }
}
let X = new Jogador("X", [], 0);
let O = new Jogador("O", [], 0);

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
    let idBotao = botao.split('-');
    let linha = idBotao[0];
    let coluna = idBotao[1];    
    // Verificar se o botão já foi clicado ou se já tem um ganhador
    console.log(idBotao);
    // for (let i = 0; i < rodada; i++) {
    //     if (X.jogadas[i] == botao || O.jogadas[i] == botao || ganhador == true) {
    //         return;
    //     }
    // }
    if (rodada == 0) {
        document.getElementById(botao).innerText = "X";
        
        rodada++;
    }
    else if (rodada % 2 == 0) {
        document.getElementById(botao).innerText = "X";
        rodada++;
        // verificarVencedor(X);
    }
    else {
        document.getElementById(botao).innerText = "O";
        // O.jogar(botao);
        rodada++;
        // verificarVencedor(O);
    }
}
// Função para verificar se houve um vencedor
const tabuleiroConferencia = () => {
    let tabuleiro = [];
    for(let i = 0; i < selectedValue; i++){
        tabuleiro[i] = [];
        for(let j = 0; j < selectedValue; j++){
            tabuleiro[i][j] = ""
        }
    }
    return tabuleiro;
}
console.log(tabuleiroConferencia());
let test = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
];