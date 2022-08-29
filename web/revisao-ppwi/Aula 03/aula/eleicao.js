// recupera o botão verificar para uma variável javascript
let btnVerificar = document.querySelector("[id=btn-verificar]");

// ação de clique do botão verificar
btnVerificar.onclick = function() {

	// recupera o ano informado pelo usuário
	let ano = document.querySelector("[id=ano]").value

	// calcula a idade do usuário
	let idade = 2022 - parseInt(ano)

	if (idade >= 16) {
		document.querySelector("[id=msg]").innerHTML = "Você poderá votar."
	} else {
		document.querySelector("[id=msg]").innerHTML = "Você não poderá votar."
	}
}