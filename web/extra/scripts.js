let vencedor = "";
var tabuleiroConferencia;
var rodada = 0;

const mensagemVitoria = document.getElementById('mensagemVitoria');
const idForm = document.getElementById('form');
const idTabuleiro = document.getElementById('tabuleiro');
const btn = document.querySelector("#send");
const selectElement = document.getElementById('tamanhoJogo');

let tamanhoJogo = selectElement.value;

let X = {
    nome: "X",
    vitorias: 0
};

let O = {
    nome: "O",
    vitorias: 0
};

criarTabuleiro();
btn.addEventListener('click', auterarNome);

selectElement.addEventListener('change', function(){
    tamanhoJogo = selectElement.value;
    // idTabuleiro.innerHTML = "";
    rodada = 0;
    vencedor = "";
    novaRodada();
    console.log(tamanhoJogo);
});
function criarTabuleiro() {
    idTabuleiro.innerHTML = '';
    criarTabuleiroConferencia()
    let tabela = document.createElement('table');
    tabela.className = "game";
    tabela.id = "tabuleiro";
    idTabuleiro.appendChild(tabela);
    let contador = 0;
    for(let i = 0; i < tamanhoJogo; i++){
        let linha = document.createElement('tr');
        tabela.appendChild(linha);
        for(let j = 0; j < tamanhoJogo; j++){
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
//function para pegar os nomes dos jogadores
function auterarNome() {
    const nome01 = document.querySelector("#nome01");
    const nome02 = document.querySelector("#nome02");

    if(nome01.value == "" || nome02.value == ""){
        X.nome = "X";
        O.nome = "O";
        document.getElementById('jogador1').innerText = X.nome;
        document.getElementById('jogador2').innerText = O.nome;
        return;
    }   
    X.nome = nome01.value;
    O.nome = nome02.value;
    document.getElementById('jogador1').innerText = X.nome;
    document.getElementById('jogador2').innerText = O.nome;
}
// Função para aceitar o clique do botão
function clique(botao) {
    let idBotao = botao.split('-');
    let linha = idBotao[0];
    let coluna = idBotao[1];    
    // Verificar se o botão já foi clicado ou se já tem um ganhador

    if (tabuleiroConferencia[linha][coluna] != "" || vencedor != "" ) {
        console.log(tabuleiroConferencia);
        console.log(vencedor);
        console.log(rodada);
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
    for(let i = 0; i < tamanhoJogo; i++){
        tabuleiroConferencia[i] = [];
        for(let j = 0; j < tamanhoJogo; j++){
            tabuleiroConferencia[i][j] = ""
        }
    }
}
// Função para verificar se houve um vencedor
function verificarVencedor() {
    
    let valorDiagonalPrincipal = tabuleiroConferencia[0][0];
    let valorDiagonalSecundaria = tabuleiroConferencia[0][tamanhoJogo- 1];

    // Verificar linhas e colunas
    for (let i = 0; i < tamanhoJogo; i++) {
        if (tabuleiroConferencia[i].every(cell => cell === tabuleiroConferencia[i][0] && cell !== "")) {
            vencedor = tabuleiroConferencia[i][0] === 'X' ? X : O;;
            vencedor.vitorias += 1;
            break;
        }

        // Verificar colunas
        if (tabuleiroConferencia.every(row => row[i] === tabuleiroConferencia[0][i] && row[i] !== "")) {
            vencedor = tabuleiroConferencia[0][i] === 'X' ? X : O;
            vencedor.vitorias += 1;
            break;
        }
        
    }
    
    if (valorDiagonalPrincipal !== "") {
        let diagonalVence = true;
        for (let i = 1; i < tamanhoJogo; i++) {
            if (tabuleiroConferencia[i][i] !== valorDiagonalPrincipal) {
                diagonalVence = false;

                break;
            }
        }
        if (diagonalVence) {
            vencedor = valorDiagonalPrincipal === 'X' ? X : O;
            vencedor.vitorias += 1;
        }
    }
    if (valorDiagonalSecundaria !== "") {
        let diagonalVence = true;
        for (let i = 1; i < tamanhoJogo; i++) {
            if (tabuleiroConferencia[i][tamanhoJogo - i - 1] !== valorDiagonalSecundaria) {
                diagonalVence = false;
                break;
            }
        }
        if (diagonalVence) {
            vencedor = valorDiagonalSecundaria === 'X' ? X : O;
            vencedor.vitorias += 1;
        }
    }

    if (vencedor) {
        console.log("Vencedor:", vencedor);
        mensagemVencedor(`O ganhador foi ${vencedor.nome}`);
        document.getElementById('placar1').innerText = X.vitorias;
        document.getElementById('placar2').innerText = O.vitorias;
    }
        if (rodada == tamanhoJogo * tamanhoJogo && vencedor == "") {
        mensagemVencedor("O jogo deu velha");
        console.log("Deu velha");
    }

}

function novaRodada(){
    rodada = 0;
    vencedor = "";
    criarTabuleiro();
    mensagemVitoria.innerHTML = '';
}
function reiniciar(){
    rodada = 0;
    vencedor = "";
    criarTabuleiro();
    X.vitorias = 0;
    O.vitorias = 0;
    document.getElementById('placar1').innerText = X.vitorias;
    document.getElementById('placar2').innerText = O.vitorias;
    
    mensagemVitoria.innerHTML = '';
}
// Função para mostrar uma mensagem de vitoria ou empate
function mensagemVencedor(message) {
    let escrever = document.createElement('div');
    escrever.className = "mensagem";
    escrever.innerText = message;

    let botao = document.createElement('button');
    botao.className = "restart";
    botao.setAttribute('onclick', `novaRodada()`);
    botao.innerText = "Nova Rodada";

    let botao2 = document.createElement('button');
    botao2.className = "stop";
    botao2.setAttribute('onclick', `reiniciar()`);
    botao2.innerText = "Reiniciar";

    mensagemVitoria.appendChild(escrever);
    mensagemVitoria.appendChild(botao);
    mensagemVitoria.appendChild(botao2);
}