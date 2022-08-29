var btnCalcular = document.querySelector('[id=btn-calcular]');

// realiza o cálculo
btnCalcular.onclick = function() {

  	let quantidade = document.getElementById("quantidade").value;
  	let total = 0;

  	if (parseInt(quantidade) >= 12) {
  		total = quantidade * 0.25;
  	} else {
  		total = quantidade * 0.3;
  	}

	document.querySelector('[id=msg]').innerHTML = "Total a pagar R$ " + total.toFixed(2);
}
