// recupera todos os itens relacionados às classes de movimentação
let aPagar = document.getElementsByClassName("a-pagar");
let aReceber = document.getElementsByClassName("a-receber");
let despesas = document.getElementsByClassName("despesa");
let receitas = document.getElementsByClassName("receita");

// declara e inicializa uma variáveis de soma
let somaAPagar = 0;
let somaAReceber = 0;
let somaDespesas = 0;
let somaReceitas = 0;

// para cada item dentro da lista de a pagar
for (let item of aPagar) {
    // adiciona o valor do item à variável de soma
    if (item.textContent !== "") {
        somaAPagar += parseFloat( item.textContent.replace(",", ".") );
    }
}

// para cada item dentro da lista de a receber
for (let item of aReceber) {
    // adiciona o valor do item à variável de soma
    if (item.textContent !== "") {
        somaAReceber += parseFloat( item.textContent.replace(",", ".") );
    }
}

// para cada item dentro da lista de despesas
for (let item of despesas) {
    // adiciona o valor do item à variável de soma
    if (item.textContent !== "") {
        somaDespesas += parseFloat( item.textContent.replace(",", ".") );
    }
}

// para cada item dentro da lista de receitas
for (let item of receitas) {
    // adiciona o valor do item à variável de soma
    if (item.textContent !== "") {
        somaReceitas += parseFloat( item.textContent.replace(",", ".") );
    }
}

// exibe o valor da soma no elemento de id #a-pagar
document.getElementById("a-pagar").innerHTML = somaAPagar.toFixed(2).replace(".", ",");
document.getElementById("a-receber").innerHTML = somaAReceber.toFixed(2).replace(".", ",");
document.getElementById("despesa").innerHTML = somaDespesas.toFixed(2).replace(".", ",");
document.getElementById("receita").innerHTML = somaReceitas.toFixed(2).replace(".", ",");