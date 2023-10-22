var jogadorX = [];
var jogadorO = [];
var rodada = 0;
var id = 0;

function clique(botao) {
    let id = +botao.id;
    console.log(id);
    if (rodada == 0) {
        document.getElementById(id).innerText = "X";
        jogadorX.push(id);
        rodada++;
    }
    // Verificar se o botão já foi clicado
    for (let i = 0; i < jogadorX.length; i++) {
        if (jogadorX[i] == id || jogadorO[i] == id) {
            return; // Sair da função sem fazer nada
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
function verificarVencedor(jogador) {
    // Definir as possíveis combinações vencedoras
    var comb = [
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
    if (rodada >= 5){
        if(jogador == "X"){
            for (let i = 0; i < comb.length; i++) {
                if (jogadorX.includes(comb[i][0]) && jogadorX.includes(comb[i][1]) && jogadorX.includes(comb[i][2])) {   
                    alert(`O jogador ${jogador} venceu!`);
                    window.location.reload();
                    break;
                }
            }
        }else{
            for (let i = 0; i < comb.length; i++) {
                if (jogadorO.includes(comb[i][0]) && jogadorO.includes(comb[i][1]) && jogadorO.includes(comb[i][2])) {  
                    alert(`O jogador ${jogador} venceu!`);
                    window.location.reload();
                    break;
                }
            }
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