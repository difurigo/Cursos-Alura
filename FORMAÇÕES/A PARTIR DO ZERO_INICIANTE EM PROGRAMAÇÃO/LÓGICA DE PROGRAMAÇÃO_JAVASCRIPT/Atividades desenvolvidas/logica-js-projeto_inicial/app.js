// Código aprendido na aula (Fiz algumas coisas a mais, pois estava muito simples)
alert("Boas vindas ao jogo do número secreto!");
let numeroSecreto = 11;
let chute = prompt("Digite um número entre 1 e 20:");

if (chute == numeroSecreto) {
    console.log("Você acertou! O número era 11");
} else {
    if (chute > numeroSecreto) {
        alert("Você errou. O número que pensei é menor.");
    } else {
        alert("Você errou. O número que pensei é maior.");
    }
    window.location.reload();
}