let listaNumerosAleatorios = [];
function sortearNumero(numeroMaximo, numeroMinimo) {
    let numeroGerado = parseInt((Math.random() * numeroMaximo) + 1);
    while (numeroGerado <= numeroMinimo) {
        numeroGerado = parseInt((Math.random() * numeroMaximo) + 1);
    }
    return numeroGerado;
}

function sortear() {
    let quantidadeDeNumeros = parseInt(document.getElementById("quantidade").value);
    let numeroMinimo = parseInt(document.getElementById("de").value);
    let numeroMaximo = parseInt(document.getElementById("ate").value);
    let contador = 0;

    while (contador < quantidadeDeNumeros) {
        let numeroGerado = sortearNumero(numeroMaximo, numeroMinimo);
        if (listaNumerosAleatorios.includes(numeroGerado)) {
            numeroGerado = sortearNumero(numeroMaximo, numeroMinimo);
        } else {
            listaNumerosAleatorios.push(numeroGerado);
        }
        contador++;
    }
}

console.log(listaNumerosAleatorios);

function reiniciar() {
    document.getElementById("btn-reiniciar").setAttribute("disabled", true);
}