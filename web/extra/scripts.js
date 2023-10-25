var ganhador = false;
var rodada = 0;
const alert = document.getElementById('alert');
const idForm = document.getElementById('form');
const btn = document.querySelector("#send");
let selectElement = document.getElementById('statusRegistro');
let selectedValue = selectElement.value;
console.log(selectedValue);

selectElement.addEventListener('change', function() {
    selectedValue = selectElement.value;
    // Agora, a variável selectedValue será atualizada toda vez que uma nova opção for selecionada.
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

let X = new Jogador("X", [], 0);
let O = new Jogador("O", [], 0);

//function para pegar os nomes dos jogadores
btn.addEventListener('click', function(e) {
    e.preventDefault();
    const nome = document.querySelector("#nome01");
    const nome02 = document.querySelector("#nome02");
    //verificar se os campos estão vazios
    if(nome.value == "" || nome02.value == ""){
        X.nome = "X";
        O.nome = "O";
        document.getElementById('jogador1').innerText = X["nome"];
        document.getElementById('jogador2').innerText = O["nome"];
        return;
    }   
    X.nome = nome.value;
    O.nome = nome02.value;
    document.getElementById('jogador1').innerText = X["nome"];
    document.getElementById('jogador2').innerText = O["nome"];

});

// Função para aceitar o clique do botão
function clique(botao) {
    let id = +botao.id;
    // Verificar se o botão já foi clicado ou se já tem um ganhador
    for (let i = 0; i < X.jogadas.length; i++) {
        if (X.jogadas[i] == id || O.jogadas[i] == id || ganhador == true) {
            return;
        }
    }
    if (rodada == 0) {
        document.getElementById(id).innerText = "X";
        X.jogar(id);
        rodada++;
    } else if (rodada % 2 == 0) {
        document.getElementById(id).innerText = "X";
        X.jogar(id);
        rodada++;
        verificarVencedor(X);
    } else {
        document.getElementById(id).innerText = "O";
        O.jogar(id);
        rodada++;
        verificarVencedor(O);
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
        if(jogador == X){
            correrLista(X.jogadas);
        }else{
            correrLista(O.jogadas);
        }
    }
    function correrLista(lista){
        for (let i = 0; i < comb.length; i++) {
            if (lista.includes(comb[i][0]) && lista.includes(comb[i][1]) && lista.includes(comb[i][2])) {  
                ganhador = true;
                mensagemAlerta(`O Jogador ${jogador.nome} Venceu!`);
                jogador.ganhar();
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
