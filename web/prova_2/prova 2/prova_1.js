
var tarefa = document.getElementsByClassName('tarefa');


let somatarefa = 0;


for(let item of tarefa) {
    somatarefa += 1
}


// document.getElementById("soma").innerHTML = somatarefa ;
document.getElementById("total").innerHTML = somatarefa ;