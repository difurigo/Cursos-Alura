// Código aprendido na aula (Fiz algumas coisas a mais, pois estava muito simples)
alert("Boas vindas ao jogo do número secreto!");
let numeroSecreto = 11;
console.log(numeroSecreto);
let chute = prompt("Digite um número entre 1 e 20:");

if (chute == numeroSecreto) {
    alert(`Você acertou! O número era ${numeroSecreto}!`);
} else {
    if (chute > numeroSecreto) {
        // Template String:
        alert("Você errou. O número que pensei é menor.");
    } else {
        alert("Você errou. O número que pensei é maior.");
    }
    window.location.reload();
} 