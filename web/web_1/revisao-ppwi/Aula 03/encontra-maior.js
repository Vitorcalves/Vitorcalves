var btnEncontrar = document.querySelector('[id=btn-encontrar]');

// realiza o cálculo
btnEncontrar.onclick = function() {

  	const valores = [
  		document.getElementById("v1").value, 
  		document.getElementById("v2").value, 
  		document.getElementById("v3").value
	]

  	let max = valores[0]

  	for (var i = 0; i < valores.length; i++) {
		if (valores[i] > max) {
			max = valores[i]
		}
	} 

	document.querySelector('[id=msg]').innerHTML = max;
}
