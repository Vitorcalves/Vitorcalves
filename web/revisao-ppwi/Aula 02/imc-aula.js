// captura o botão (HTML) que realizará o cálculo do IMC
var btnCalcular = document.querySelector('[id=btnCalcular]');

// ação de clique do botão calcular IMC
btnCalcular.onclick = function() {

	// recupera os valores dos inputs
	let peso = document.querySelector('[id=peso]').value;
	let altura = document.querySelector('[id=altura]').value.replace(",", ".");

	// validação
	if ( peso === "" ) {
		alert("Informe o peso.");
		return;
	}

	if ( altura === "" ) {
		alert("Informe a altura.");
		return;
	}

	// calcula o imc
	let imc = parseFloat(peso) / (parseFloat(altura) * parseFloat(altura));

	// define o status (categoria) do imc do usuário
	let status = "";

	if ( imc < 20.7 ) {
		status = "abaixo do peso.";
	} else if (imc >= 20.7 && imc < 26.4) {
		status = "no peso normal.";
	} else if (imc >= 26.4 && imc < 27.8) {
		status = "pouco acima do peso.";
	} else if (imc >= 27.8 && imc < 31.1) {
		status = "acima do peso."
	} else {
		status = "obeso."
	}

	alert("O IMC é de " + imc.toFixed(2) + " você está " + status);
}