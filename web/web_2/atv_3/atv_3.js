// captura os botoes do html
var btnSomar = document.querySelector('[id=btnSomar]')
var btnSubtracao = document.querySelector('[id=btnSubtrair]')
var btnMultiplicar = document.querySelector('[id=btnMultiplicar]')
var btnDivisao = document.querySelector('[id=btnDividir]')

// ação de clique do botão somar
btnSomar.onclick = function(){
	// recupera os valores dos inputs
	let valor1 = document.querySelector('[name=valor1]').value;
	let valor2 = document.querySelector('[name=valor2]').value;

	// validação do primeiro input
	if ( valor1 === ""){
		alert("Informe um valor para o primeiro campo.");
		return;
	}

	// validação do segundo input
	if ( valor2 === ""){
		alert("Informe um valor para o primeiro campo.");
		return;
	}

	// variável para obter a soma dos dois valores
	let resultado = parseInt(valor1) + parseInt(valor2);

	// exibe o valor da soma na tela
	alert("A soma entre os dois valores é de " + resultado);
}