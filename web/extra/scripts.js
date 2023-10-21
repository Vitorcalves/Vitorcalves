var valores = [];
var rodada = 0;
var id = 0;
function clique1(button) {
    if (rodada%2==0) {
        button.textContent = "X";
    } else {
        button.textContent = "O";
    }
    rodada++;
}

function clique() {
    id = document.getElementById(event.target.id).id;
    // Verificar se o botão já foi clicado
    if (valores[id] == "") {
        if (rodada % 2 == 0) {
            document.getElementById(id).innerText = "X";
            valores[id] = "X";
        } else {
            document.getElementById(id).innerText = "O";
            valores[id] = "O";
        }
        rodada++;
        // Verificar se há um vencedor
        verificarVencedor();
    }
}

function verificarVencedor() {
    // Definir as possíveis combinações vencedoras
    var combinacoes = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];
    // Percorrer as combinações e comparar com os valores
    for (let i = 0; i < combinacoes.length; i++){
        if (valores[combinacoes[i][0]] != "" && valores[combinacoes[i][0]] == valores[combinacoes[i][1]] && valores[combinacoes[i][1]] == valores[combinacoes[i][2]]) {
            // Mostrar uma mensagem de vitória
            alert(`O jogador ${valores[combinacoes[i][0]]} venceu!`);
    
            // Reiniciar o jogo
            window.location.reload();
            break;
        }
    }
    // Verificar se houve empate
    if (rodada == 9) {
        // Mostrar uma mensagem de empate
        alert("O jogo terminou em empate!");
        // Reiniciar o jogo
        window.location.reload();
    }
}
