// Crie uma função que calcule o índice de massa corporal (IMC) de uma pessoa, a partir de sua altura, em metros, e peso, em quilogramas, que serão recebidos como parâmetro.
function calculaImc(altura, peso) {
    let imc = peso / altura ** 2;
    return imc;
}

// Crie uma função que calcule o valor do fatorial de um número passado como parâmetro.
function calculaFatorial(numero) {
    if (numero === 0 || numero === 1) {
        return 1;
    }
    
    let resultado = 1;
    for (numero; numero > 0; numero--) {
        resultado *= numero;
    }
    return resultado;
}

// Crie uma função que converte um valor em dólar, passado como parâmetro, e retorna o valor equivalente em reais. Para isso, considere a cotação do dólar igual a R$4,80.
function converterDolarEmReais(valor) {
    const real = 4.80;
    let valorConvertido = valor * real;
    return valorConvertido;
}

// Crie uma função que mostre na tela a área e o perímetro de uma sala retangular, utilizando altura e largura que serão dadas como parâmetro.
function calcularAreaRetangulo(altura, largura) {
    let area = altura * largura;
    return area;
}

function calcularPerimetroRetangulo(altura, largura) {
    let perimetro = (altura * 2) + (largura * 2);
    return perimetro;
}

function calcularPropriedadesRetangulares(altura, largura) {
    console.log("A área do retângulo é: " + calcularArea(altura, largura));
    console.log("O perímetro do retângulo é: " + calcularPerimetro(altura, largura));
}

// Crie uma função que mostre na tela a área e o perímetro de uma sala circular, utilizando seu raio que será fornecido como parâmetro. Considere Pi = 3,14.
const pi = 3.14;

function calcularAreaCirculo(raio) {
    let area = pi * (raio ** 2);
    return area;
}

function calcularPerimetroCirculo(raio) {
    let perimetro = 2 * pi * raio;
    return perimetro;
}

function calcularPropriedadesCirculares(raio) {
    console.log("A área do círculo é: " + calcularAreaCirculo(raio));
    console.log("O perímetro do círculo é: " + calcularPerimetroCirculo(raio));
}

// Crie uma função que mostre na tela a tabuada de um número dado como parâmetro.
function calcularTabuada(numero) {
    let multiplicador = 0;
    while (multiplicador <= numero) {
        let resultado = numero * multiplicador;
        console.log(`${numero} x ${multiplicador} = ${resultado}`);
        multiplicador++;
    }
}
