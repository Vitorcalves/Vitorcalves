// adiciona o recurso ao carregar todo o objeto DOM
document.addEventListener("DOMContentLoaded", () => {

    // recupera a lista de botões de inclusão/remoção
    let btnIncluirRemover = document.querySelectorAll(".btn-incluir-remover")

    // para cada botão incluir/remover
    btnIncluirRemover.forEach(function(btn){

        // adiciona um evento de clique
        btn.addEventListener("click", () => {

            // caso o atributo data-pedido esteja igual a 0, inclui o item
            if (btn.getAttribute("data-pedido") === "0") {
                // muda o valor do atributo
                btn.setAttribute("data-pedido", "1")
                // muda o texto do botão
                btn.textContent = "Remover"
            } else {
                btn.setAttribute("data-pedido", "0")
                btn.textContent = "Incluir"
            }
        })
    })

    // recupera o botão enviar pedido
    let btnEnviarPedido = document.querySelector(".btn-enviar-pedido")

    // variável para armazenar os itens do pedido
    let pedido = ""

    // adiciona um evento de clique ao botão enviar pedido
    btnEnviarPedido.addEventListener("click", () => {

        // variável para determinar o valor total do pedido
        let totalPedido = 0
        
        // verifica cada botão incluir/remover
        btnIncluirRemover.forEach(function(btn) {

            // verifica o atributo data-pedido
            if (btn.getAttribute("data-pedido") === "1") {

                // armazena a quantidade pedida do produto
                let quantidade = parseInt(
                    document.querySelector(
                        ".quantidade[data-codigo-quantidade='" + 
                        btn.getAttribute("data-codigo") + "']").value
                )

                // armazena o nome do produto
                let produto = btn.getAttribute("data-produto")

                // recupera o valor do item
                let valor = parseFloat( btn.getAttribute("data-valor") ).toFixed(2)

                // subtotal do item
                let subtotal = (quantidade * valor).toFixed(2)

                // adiciona o valor ao total do pedido
                // totalPedido = totatotalPedido + subtotal
                totalPedido += parseFloat(subtotal)

                // adiciona a quantidade e produto ao pedido
                pedido += quantidade + " - " + produto + " x " + valor + " = " + 
                        subtotal + "<br>"
            }
        })

        // se o pedido estiver vazio
        if (pedido === "") {
            document.getElementById("modal-pedido-msg").textContent 
                = "Inclua uma mensagem"
        } else {
            // concatena o valor total à string do pedido
            pedido += "Total do pedido: R$ <b>" + totalPedido.toFixed(2) + "</b>"
            // inclui os itens do pedido no modal
            document.getElementById("modal-pedido-msg").innerHTML = pedido;
        }

        // cria um modal e exibe o pedido na tela
        const meuModal = new bootstrap.Modal(
            document.getElementById("modal-pedido"), {}
        )
        // exibe o modal na tela
        meuModal.show()

    })

    // recupera o botão de confirmação de pedido
    let btnConfirmarPedido = document.getElementById("btn-enviar-pedido")

    // ação de clique no botão confirmar pedido
    btnConfirmarPedido.addEventListener("click", () => {
        // redireciona o usuário para o WhatsApp
        window.location.href = "https://wa.me/5532984355406?text=" +
            encodeURI(pedido.replace(/<br\s*[\/]?>/gi, "\n"))
    })

})