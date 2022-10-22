// recupera o botão calcular
let btnCalcular = document.querySelector("[id=btn-calcular]");

// realiza o cálculo
btnCalcular.onclick = function() {

	// recupera a quantidade informada pelo usuário
	let quantidade = document.querySelector("[id=quantidade]").value

	// inicializa a variável total
	let total = 0

	if (parseInt(quantidade) >= 12) {
		total = quantidade * 0.25;
	} else {
		total = quantidade * 0.3;
	}

	// exibe o valor total ao usuário
	document.querySelector("[id=msg]").innerHTML = "Total a pagar R$ " + total.toFixed(2)
}