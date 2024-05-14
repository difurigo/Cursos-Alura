function exibirTexto(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

function verificarChute() {
    let chute = document.querySelector("input").value;
    console.log(chute == numeroSecreto);
}

function gerarNumeroAleatorio() {
    return parseInt((Math.random() * 10) + 1);
}

exibirTexto("h1", "Jogo do Número Secreto");
exibirTexto("p", "Digite um número entre 1 e 10");

let numeroSecreto = gerarNumeroAleatorio();
