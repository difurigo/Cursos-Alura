// Código aprendido na aula (Fiz algumas coisas a mais, pois estava muito simples)
alert("Boas vindas ao jogo do número secreto!");
let numeroSecreto = 11;
console.log(numeroSecreto);
let chute;
let tentativas = 1;

while (chute != numeroSecreto) {
    chute = prompt("Digite um número entre 1 e 20:");
    if (chute == numeroSecreto) {
        // Template String:
        alert(`Você acertou! O número era ${numeroSecreto}! Foram ${tentativas} tentativas.`);
    } else {
        if (chute > numeroSecreto) {
            alert("Você errou. O número que pensei é menor.");
        } else {
            alert("Você errou. O número que pensei é maior.");
        }
        tentativas++;
    } 
}