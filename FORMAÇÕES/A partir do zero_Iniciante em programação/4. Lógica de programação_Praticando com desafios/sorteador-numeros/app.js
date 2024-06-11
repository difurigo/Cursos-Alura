function alterarTexto(id, texto) {
    let textoAlterado = document.getElementById(id);
    textoAlterado.innerHTML = texto;
}

function sortearNumero(numeroMaximo, numeroMinimo) {
    return Math.floor(Math.random() * (numeroMaximo - numeroMinimo + 1)) + numeroMinimo;
}

function alterarStatusBotao(id) {
    let botao = document.getElementById(id);
    if (botao.classList.contains("container__botao-desabilitado")) {
        botao.classList.remove("container__botao-desabilitado");
        botao.classList.add("container__botao");
    } else {
        botao.classList.remove("container__botao");
        botao.classList.add("container__botao-desabilitado");
    }
}

function sortear() {
    let quantidadeDeNumeros = parseInt(document.getElementById("quantidade").value);
    let numeroMinimo = parseInt(document.getElementById("de").value);
    let numeroMaximo = parseInt(document.getElementById("ate").value);

    let listaNumerosAleatorios = [];
    let numeroGerado;

    for (let i = 0; i < quantidadeDeNumeros; i++) {
        numeroGerado = sortearNumero(numeroMaximo, numeroMinimo);
        while (listaNumerosAleatorios.includes(numeroGerado)) {
            numeroGerado = sortearNumero(numeroMaximo, numeroMinimo);
        }
        listaNumerosAleatorios.push(numeroGerado);
    }
    
    alterarTexto("resultado", `<label class="texto__paragrafo">Números sorteados: ${listaNumerosAleatorios}</label>`);
    
    alterarStatusBotao("btn-sortear");
    alterarStatusBotao("btn-reiniciar");
}

function reiniciar() {
    document.getElementById("quantidade").value = "";
    document.getElementById("de").value = "";
    document.getElementById("ate").value = "";
    alterarTexto("resultado", `<label class="texto__paragrafo">Números sorteados: nenhum até agora</label>`);
    alterarStatusBotao("btn-sortear");
    alterarStatusBotao("btn-reiniciar");
}