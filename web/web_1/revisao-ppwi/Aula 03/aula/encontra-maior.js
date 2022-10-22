let btnEncontrar = document.querySelector("[id=btn-encontrar]");

btnEncontrar.onclick = function() {

	const valores = [
		document.getElementById("v1").value,
		document.getElementById("v2").value,
		document.getElementById("v3").value
	]

	let max = valores[0]

	for (let cont = 0; cont < valores.length; cont++ ) {
		if (valores[cont] > max) {
			max = valores[cont]
		}
	}

	document.getElementById.innerHTML = max
}