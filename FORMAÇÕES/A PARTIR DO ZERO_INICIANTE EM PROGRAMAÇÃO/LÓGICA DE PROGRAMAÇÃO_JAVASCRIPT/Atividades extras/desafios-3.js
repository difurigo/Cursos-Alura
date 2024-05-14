// Crie um contador que comece em 1 e vá até 10 usando um loop while. Mostre cada número.
let contadorPositivo = 1;
while (contadorPositivo <= 10) {
    console.log(contadorPositivo);
    contadorPositivo++;
}

// Crie um contador que começa em 10 e vá até 0 usando um loop while. Mostre cada número.
let contadorNegativo = 10;
while (contadorNegativo >= 0) {
    console.log(contadorNegativo);
    contadorNegativo--;
}

// Crie um programa de contagem regressiva. Peça um número e conte deste número até 0, usando um loop while no console do navegador.
let numeroMaximo = parseInt(prompt("Digite um número: "));
while (numeroMaximo >= 0) {
    console.log(numeroMaximo);
    numeroMaximo--;
}

// Crie um programa de contagem progressiva. Peça um número e conte de 0 até esse número, usando um loop while no console do navegador.
let numero = parseInt(prompt("Digite um número: "));
let contadorProgressivo = 0;
while (contadorProgressivo <= numero) {
    console.log(contadorProgressivo);
    contadorProgressivo++;
}
