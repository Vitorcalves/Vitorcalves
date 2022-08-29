let btnEncontrar = document.querySelector("[id = botao]")
btnEncontrar.onclick = function() {
    const idades = [
        document.getElementById("idade1").value, 
        document.getElementById("idade2").value, 
        document.getElementById("idade3").value,
        document.getElementById("idade4").value,
        document.getElementById("idade5").value,
        
    ]
    let apto = 0
    for (var i = 0; i < idades.length; i++) {
        if ( idades[i] > 16 ){
            apto = apto + 1
        } 

		
	}
    alert("as pessoas aptas a voatar sao " + apto + " pessoas ");
}