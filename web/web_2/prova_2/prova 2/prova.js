// recupera todos os itens relacionados às classes de movimentação
let aPagar = document.getElementsByClassName("a-pagar");


// declara e inicializa uma variáveis de soma
let somaAPagar = 0;


// para cada item dentro da lista de a pagar
for(let item of aPagar) {
    somaAPagar += parseFloat (item.textContent.replace(",", "."))
}
total = somaAPagar * 0.05
total2 = somaAPagar - total


// exibe o valor da soma no elemento de id #a-pagar
document.getElementById("soma").innerHTML = somaAPagar.toFixed(2).replace(".", ",");
document.getElementById("total").innerHTML = total2.toFixed(2).replace(".", ",");