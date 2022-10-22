var btnEncontrar = document.querySelector('[id=btn-calcular]');

// realiza o cálculo
btnEncontrar.onclick = function() {

  	const valores = [
  		document.getElementById("v1").value, 
  		document.getElementById("v2").value, 
  		document.getElementById("v3").value,
  		document.getElementById("v4").value,
  		document.getElementById("v5").value,
  		document.getElementById("v6").value,
  		document.getElementById("v7").value,
  		document.getElementById("v8").value,
  		document.getElementById("v9").value,
  		document.getElementById("v10").value
	]

  	let soma = 0

  	for (var i = 0; i < valores.length; i++) {
		soma += parseFloat(valores[i])
	}

	let media = soma / valores.length

	document.querySelector('[id=msg]').innerHTML = "A média dos valores é " + media;
}