function calculaImc(peso, altura) {
	return Math.round(peso / (altura * altura));
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#calcular").addEventListener("click", function() {
        let nomeInformado = document.getElementById('nome').value;
        let pesoInformado = parseFloat(document.getElementById('peso').value);
        let alturaInformada = parseFloat(document.getElementById('altura').value);
        let imc = calculaImc(pesoInformado, alturaInformada);

        let resultado = nomeInformado + ", o resultado do seu IMC é " + imc + ".";

        if (imc < 18.5) {
            resultado += "\nSeu IMC está abaixo do recomendado.";
        } else if (imc > 35) {
            resultado += "\nSeu IMC está acima do recomendado.";
        } else {
            resultado += "\nSeu IMC está dentro do recomendado.";
        }

        document.getElementById('resultado').innerText = resultado;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#recarregar").addEventListener("click", function() {
        window.location.reload();
    });
});