// atribui o botão calcular a uma variável do javascript
let btnCalcular = document.querySelector('[id=btn-calcular]')

// adiciona uma funcionalidade ao clique do botão calcular
btnCalcular.onclick = function(){

	// cria um vetor contendo todos os valores dos inputs da página
	const valores = [
		document.getElementById('v1').value,
		document.getElementById('v2').value,
		document.getElementById('v3').value,
		document.getElementById('v4').value,
		document.getElementById('v5').value,
		document.getElementById('v6').value,
		document.getElementById('v7').value,
		document.getElementById('v8').value,
		document.getElementById('v9').value,
		document.getElementById('v10').value
	]

	// declara a variável soma inicializando-a em zero
	let soma = 0

	// laço de repetição para percorrer todos os elementos do vetor
	for ( let cont = 0 ; cont < valores.length ; cont++ ) {
		// acrescenta o valor do elemento na variável soma
		soma += parseFloat(valores[cont])
	}

	// encontra a média dos valores
	let media = soma / valores.length

	// exibe a mensagem com a média dos valores na tela
	document.querySelector('[id=msg]').innerHTML = 'A média é ' + media
}