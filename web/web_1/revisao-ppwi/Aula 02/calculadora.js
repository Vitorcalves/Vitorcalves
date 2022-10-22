// captura os botões do HTML
var btnSomar = document.querySelector('[id=btnSomar]');
var btnSubtrair = document.querySelector('[id=btnSubtrair]');
var btnMultiplicar = document.querySelector('[id=btnMultiplicar]');
var btnDividir = document.querySelector('[id=btnDividir]');

// ação de clique do botão somar
btnSomar.onclick = function() {
	// recupera os valores dos inputs
	let valor1 = document.querySelector('[name=valor1]').value;
	let valor2 = document.querySelector('[name=valor2]').value;

	// validação do primeiro input
	if ( valor1 === "" ) {
		alert("Informe um valor para o primeiro campo.");
		return;
	}

	// validação do segundo input
	if ( valor2 === "" ) {
		alert("Informe um valor para o segundo campo.");
		return;
	}

	// variável para obter a soma entre os dois valores
	let resultado = parseInt(valor1) + parseInt(valor2);

	// exibe o valor da soma na tela
	alert("A soma entre os dois valores é de " + resultado);
}

// ação de clique para o botão subtrair
btnSubtrair.onclick = function() {
	// recupera os valores dos inputs
	let valor1 = document.querySelector('[name=valor1]').value;
	let valor2 = document.querySelector('[name=valor2]').value;

	// validação do primeiro input
	if ( valor1 === "" ) {
		alert("Informe um valor para o primeiro campo.");
		return;
	}

	// validação do segundo input
	if ( valor2 === "" ) {
		alert("Informe um valor para o segundo campo.");
		return;
	}

	// variável para obter a subtração entre os dois valores
	let resultado = parseInt(valor1) - parseInt(valor2);

	// exibe o valor da subtração na tela
	alert("A subtração entre os dois valores é de " + resultado);
}

// ação de clique para o botão multiplicar
btnMultiplicar.onclick = function() {
	// recupera os valores dos inputs
	let valor1 = document.querySelector('[name=valor1]').value;
	let valor2 = document.querySelector('[name=valor2]').value;

	// validação do primeiro input
	if ( valor1 === "" ) {
		alert("Informe um valor para o primeiro campo.");
		return;
	}

	// validação do segundo input
	if ( valor2 === "" ) {
		alert("Informe um valor para o segundo campo.");
		return;
	}

	// variável para obter a multiplicação entre os dois valores
	let resultado = parseInt(valor1) * parseInt(valor2);

	// exibe o valor da multiplicação na tela
	alert("A multiplicação entre os dois valores é de " + resultado);
}

// ação de clique do botão dividir
btnDividir.onclick = function() {
	// recupera os valores dos inputs
	let valor1 = document.querySelector('[name=valor1]').value;
	let valor2 = document.querySelector('[name=valor2]').value;

	// validação do primeiro input
	if ( valor1 === "" ) {
		alert("Informe um valor para o primeiro campo.");
		return;
	}

	// validação do segundo input
	if ( valor2 === "" ) {
		alert("Informe um valor para o segundo campo.");
		return;
	}

	// variável para obter a divisão entre os dois valores
	let resultado = parseFloat(valor1) / parseFloat(valor2);

	// exibe o valor da divisão na tela
	alert("A divisão entre os dois valores é de " + resultado);
}