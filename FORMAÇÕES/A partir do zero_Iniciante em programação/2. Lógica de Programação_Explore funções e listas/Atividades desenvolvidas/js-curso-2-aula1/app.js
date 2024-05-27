function limparCampo(campo) {
    campo = document.querySelector("input");
    campo.value = "";
}

function exibirTexto(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

function verificarChute() {
    let chute = document.querySelector('input').value;
    
    if (chute == numeroSecreto) {
            exibirTexto('h1', 'Acertou!');
            let palavraTentativa = tentativas > 1 ? 'tentativas': 'tentativa';
            let mensagemTentativas = `Você descobriu o número secreto com ${tentativas} ${palavraTentativa}!`; 
            exibirTexto('p', mensagemTentativas);
            document.getElementById("reiniciar").removeAttribute("disabled");
            console.log(listaNumerosAleatorios);
    } else {
            if (chute > numeroSecreto) { 
                exibirTexto ('p', 'O número secreto é menor');
            } else {
                exibirTexto('p', 'O número secreto é maior');
            }
            tentativas++;
            limparCampo(chute);
    }
}

let listaNumerosAleatorios = [];
function gerarNumeroAleatorio() {
    let numeroMaximo = 10;
    let numeroGerado = parseInt((Math.random() * numeroMaximo) + 1);
    let qtdElementosLista = listaNumerosAleatorios.length;

    if (qtdElementosLista == numeroMaximo) {
        listaNumerosAleatorios = [];
    }    

    if (listaNumerosAleatorios.includes(numeroGerado)) {
        return gerarNumeroAleatorio();
    } else {
        listaNumerosAleatorios.push(numeroGerado);
        return numeroGerado;
    }
}

function exibirMensagemInicial() {
    exibirTexto("h1", "Jogo do Número Secreto");
    exibirTexto("p", "Digite um número entre 1 e 10");
}

function novoJogo() {
    numeroSecreto = gerarNumeroAleatorio();
    limparCampo();
    tentativas = 1;
    exibirMensagemInicial();
    document.getElementById("reiniciar").setAttribute("disabled", true);
}

let tentativas = 1;
let numeroSecreto = gerarNumeroAleatorio();
exibirMensagemInicial();
 