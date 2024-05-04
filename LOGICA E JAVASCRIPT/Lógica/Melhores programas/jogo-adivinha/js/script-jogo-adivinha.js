function sorteia(n) {
    return Math.floor(Math.random() * (n + 1));
}

function sorteiaNumeros(quantidade, n) {
    let numeros = new Set();
    while (numeros.size < quantidade) {
        let numeroAleatorio = sorteia(n);
        if (numeroAleatorio !== 0) {
            numeros.add(numeroAleatorio);
        }
    }
    return Array.from(numeros);
}

function verificaChute1(numero, tentativas) {
    let chute = parseInt(document.querySelector("#chute").value);
    if (isNaN(chute)) {
        alert("Por favor, digite um número antes de verificar.");
        return;
    }

    if (chute == numero) {
        alert("UAU! Você acertou, pois eu pensei no " + numero + " mesmo!");
        alert("Clique em 'Jogar novamente' para jogar mais uma.");
    } else {
        if ((tentativas - 1) > 0) {
            alert("Você errou! Você ainda tem " + (tentativas - 1) + " tentativa(s) restante(s).");
        } else {
            alert("Suas tentativas acabaram. Eu tinha pensado no " + numero);
            alert("Clique em 'Jogar novamente' para jogar mais uma.");
        }
    }
}

function verificaChute2(numeros, tentativas) {
    let chute = parseInt(document.querySelector("#chute").value);
    if (isNaN(chute)) {
        alert("Por favor, digite um número antes de verificar.");
        return;
    } else {
        let acertou = false;
        for (let posicao = 0; posicao < numeros.length; posicao++) {
            if (chute == numeros[posicao]) {
                alert("UAU! Você acertou, pois eu pensei nestes números: " + numeros);
                acertou = true;
                break;
            }
        }

        if(acertou) {
            alert("Clique em 'Jogar novamente' para jogar mais uma.");
        } else {
            if (tentativas - 1 > 0) {
                alert("Você errou! Você ainda tem " + (tentativas - 1) + " tentativa(s) restante(s).");
            } else {
                alert("Suas tentativas acabaram. Os números que pensei eram: " + numeros);
                alert("Clique em 'Jogar novamente' para jogar mais uma.");
            }
            document.querySelector("#chute").value = 0;
            document.querySelector("#chute").focus();
        }
    }
}


function iniciarJogo1(numero, maxTentativas) {
    let tentativas = maxTentativas;

    document.querySelector("#chute").value = 0;
    document.querySelector("#chute").focus();

    document.querySelector("#rodar").addEventListener("click", function () {
        verificaChute1(numero, tentativas);
        tentativas--;
    });
}

function iniciarJogo2(numeros, maxTentativas) {
    let tentativas = maxTentativas;

    document.querySelector("#chute").value = 0;
    document.querySelector("#chute").focus();

    document.querySelector("#rodar").addEventListener("click", function () {
        verificaChute2(numeros, tentativas);
        tentativas--;
    });
}

function increment() {
    const input = document.getElementById("chute");
    if (parseInt(input.value) < 10) {
        input.value = parseInt(input.value) + 1;
    }
}

function decrement() {
    const input = document.getElementById("chute");
    if (parseInt(input.value) > 0) {
        input.value = parseInt(input.value) - 1;
    }
}

alert("Será que você acerta o número que eu pensei no chute?");
let dificuldade = parseInt(prompt("Primeiro vamos definir em quantos números devo pensar!\n" +
    "Digite 1 - Eu penso em apenas 1 número\n" +
    "Digite 2 - Eu penso em quantos números você definir"));

if (dificuldade === 1) {
    let maximo = 10;
    alert("Você terá 3 tentativas.\n" + "Clique em OK para começar o jogo!");
    let numero = sorteia(maximo);
    console.log(numero);
    iniciarJogo1(numero, 3);

} else if(dificuldade === 2) {
	let maximo = 10;
    let quantidadeNumeros = parseInt(prompt("Agora, escolha quantos números tenho que pensar:"));
    alert("Você terá 3 tentativas.\n" + "Clique em OK para começar o jogo!");
    let lista = sorteiaNumeros(quantidadeNumeros, maximo);
    console.log(lista);
    iniciarJogo2(lista, 3);
    
} else {
    alert("Opção inválida. Clique em 'Jogar novamente' para jogar mais uma.");
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#voltar").addEventListener("click", function() {
        window.location.href = "./index.html";
    });
});

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#recarregar").addEventListener("click", function() {
        window.location.reload();
    });
});
