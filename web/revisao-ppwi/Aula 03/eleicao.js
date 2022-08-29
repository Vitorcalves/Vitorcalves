var btnVerificar = document.querySelector('[id=btn-verificar]');

// realiza o cálculo
btnVerificar.onclick = function() {

  	let ano = document.querySelector('[id=ano]').value;
  	let idade = 2022 - parseInt(ano);

  	if (idade < 16) {
  		document.querySelector('[id=msg]').innerHTML = "Você não poderá votar esse ano.";
  	} else {
  		document.querySelector('[id=msg]').innerHTML = "Você poderá votar esse ano.";
  	}
}