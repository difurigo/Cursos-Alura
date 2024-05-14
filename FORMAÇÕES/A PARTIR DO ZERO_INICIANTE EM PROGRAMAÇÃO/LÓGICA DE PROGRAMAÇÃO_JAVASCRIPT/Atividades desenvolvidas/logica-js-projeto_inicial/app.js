// Código aprendido na aula (Fiz algumas coisas a mais, pois estava muito simples)
alert("Boas vindas ao jogo do número secreto!");
let multiplicador = 20;
let numeroSecreto = parseInt((Math.random() * multiplicador) + 1);
console.log(numeroSecreto);
let chute;
let tentativas = 1;

while (chute != numeroSecreto) {
    chute = prompt(`Digite um número entre 1 e ${multiplicador}:`);
    if (chute == numeroSecreto) {
        break;
    } else {
        if (chute > numeroSecreto) {
            alert("Você errou. O número que pensei é menor.");
        } else {
            alert("Você errou. O número que pensei é maior.");
        }
        tentativas++;
    } 
}

let variacaoTentativa = tentativas > 1 ? "tentativas." : "tentativa";
alert(`Você acertou! O número era ${numeroSecreto}! Em ${tentativas} ${variacaoTentativa}`);

// if (tentativas > 1) {
//     // Template String:
//     alert(`Você acertou! O número era ${numeroSecreto}! Foram ${tentativas} tentativas.`);
// } else {
//     alert(`Caramba você acertou de primeira! O número era ${numeroSecreto} mesmo!`);
// }
