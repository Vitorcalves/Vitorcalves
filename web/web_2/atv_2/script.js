let btnEncontrar = document.querySelector("[id = botao]")
btnEncontrar.onclick = function() {
    const notas = [
        document.getElementById("nota1").value, 
        document.getElementById("nota2").value, 
        document.getElementById("nota3").value,
        document.getElementById("nota4").value,
        
    ]
    let cont = 1
    let media = 0
    for (var i = 0; i < notas.length; i++) {
        
        media = media + (parseFloat(notas[i]) * (i +1))
        cont = cont + 1 
	}

    media = media / 10
    if( media >= 6 ){
        alert("a media do aluno foi " + media + " pontos ele esta aprovado ");
    }
    else{
        alert("a media do aluno foi " + media + " pontos ele esta reprovado ");
    }
}