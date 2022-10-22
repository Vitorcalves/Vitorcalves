var btnCalcular = document.querySelector('[id=btnCalcular]');

// realiza o cálculo
btnCalcular.onclick = function() {

  	let peso = document.querySelector('[id=peso]').value;
  	let altura = document.querySelector('[id=altura]').value.replace(",", ".");

  	if (peso === "") {
  		alert("Informe o peso");
  		return;
  	}

  	if (altura === "") {
  		alert("Informe a altura");
  		return;
  	}

	
  	let imc = (parseFloat(peso) / (parseFloat(altura) * parseFloat(altura))).toFixed(2);

  	let status = "";

  	if (imc < 20.7) {
	   status = "abaixo do peso";
	} else if (imc >= 20.7 && imc < 26.4) {
	   status = "no peso normal";
	} else if (imc >= 26.4 && imc < 27.8) {
	   status = "pouco acima do peso";
	} else if (imc >= 27.8 && imc < 31.1) {
	   status = "acima do peso";
	} else {
	   status = "obeso";
	}

  	alert("O IMC é de " + imc + " você está " + status);
}
