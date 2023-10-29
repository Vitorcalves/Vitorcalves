var ganhador = false;
var tabuleiroConferencia
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
    criarTabuleiroConferencia()
    console.log(tabuleiroConferencia);
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
let X = new Jogador("X", 0);
let O = new Jogador("O", 0);
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
    if (tabuleiroConferencia[linha][coluna] != "" || ganhador == true) {
        console.log("entrou");
        console.log(tabuleiroConferencia);
        console.log(ganhador);
        return;
    }
    else if (rodada % 2 == 0) {
        document.getElementById(botao).innerText = "X";
        rodada++;
        tabuleiroConferencia[linha][coluna] = "X";
        verificarVencedor();
    }
    else {
        document.getElementById(botao).innerText = "O";
        tabuleiroConferencia[linha][coluna] = "O";
        rodada++;
        verificarVencedor();
    }
}
// Função para verificar se houve um vencedor
function criarTabuleiroConferencia()  {
    tabuleiroConferencia = [];
    for(let i = 0; i < selectedValue; i++){
        tabuleiroConferencia[i] = [];
        for(let j = 0; j < selectedValue; j++){
            tabuleiroConferencia[i][j] = ""
        }
    }
}
function verificarVencedor() {
    let vencedor = "";
    let valorDiagonalPrincipal = tabuleiroConferencia[0][0];
    let valorDiagonalSecundaria = tabuleiroConferencia[0][selectedValue- 1];

    // Verificar linhas e colunas
    for (let i = 0; i < selectedValue; i++) {
        // Verificar linhas
        if (tabuleiroConferencia[i].every(cell => cell === tabuleiroConferencia[i][0] && cell !== "")) {
            vencedor = tabuleiroConferencia[i][0];
            
            break;
        }

        // Verificar colunas
        if (tabuleiroConferencia.every(row => row[i] === tabuleiroConferencia[0][i] && row[i] !== "")) {
            vencedor = tabuleiroConferencia[0][i];
            break;
        }
        
    }
    
    if (valorDiagonalPrincipal !== "") {
        let diagonalVence = true;
        for (let i = 1; i < selectedValue; i++) {
            if (tabuleiroConferencia[i][i] !== valorDiagonalPrincipal) {
                diagonalVence = false;

                break;
            }
        }
        if (diagonalVence) {
            vencedor = valorDiagonalPrincipal;
        }
    }
    if (valorDiagonalSecundaria !== "") {
        let diagonalVence = true;
        for (let i = 1; i < selectedValue; i++) {
            if (tabuleiroConferencia[i][selectedValue - i - 1] !== valorDiagonalSecundaria) {
                diagonalVence = false;
                break;
            }
        }
        if (diagonalVence) {
            vencedor = valorDiagonalSecundaria;
        }
    }

    if (vencedor) {
        console.log("Vencedor:", vencedor);
        mensagemAlerta(`O ganhador foi ${vencedor}`);
    } else {
        console.log("Nenhum vencedor ainda.");
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