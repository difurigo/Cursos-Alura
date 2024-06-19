function subtrairIngressos(qtdTipo, qtdEscolhida, tipoIngresso) {
    let totalPista = parseInt(qtdTipo.textContent);

    // Condicionar caso acabem os ingressos
    if (totalPista >= qtdEscolhida && totalPista > 0) {
        alert('Compra realizada com sucesso!');
        totalPista -= qtdEscolhida;
        qtdTipo.innerHTML = `${totalPista}`;
    } else {
        alert(`Quantidade indisponível para ${tipoIngresso}`);
    }
}

function comprar() {
    // Recuperar os elementos utilizados
    let tipoIngresso = document.getElementById('tipo-ingresso');
    let ingressoEscolhido = tipoIngresso.value;
    if (!ingressoEscolhido || ingressoEscolhido.trim() === '') {
        alert('Selecione um ingresso disponível.');
        return;
    }

    let quantidade = parseInt(document.getElementById('qtd').value);
    if (isNaN(quantidade) || quantidade <= 0) {
        alert('Quantidade de ingressos inválida. Verifique e tente novamente!');
        return;
    }

    // Tipos de ingresso
    let pista = tipoIngresso.querySelector('[value="pista"]').value;
    let qtdPista = document.getElementById('qtd-pista');

    let cadeiraSuperior = tipoIngresso.querySelector('[value="superior"]').value;
    let qtdSuperior = document.getElementById('qtd-superior');

    let cadeiraInferior = tipoIngresso.querySelector('[value="inferior"]').value;
    let qtdInferior = document.getElementById('qtd-inferior');

    // Descobrir qual é o tipo de ingresso
    if (ingressoEscolhido == pista) {
        // Subtrair a quantidade de ingressos
        subtrairIngressos(qtdPista, quantidade, ingressoEscolhido);

    } else if (ingressoEscolhido == cadeiraSuperior) {
        // Subtrair a quantidade de ingressos
        subtrairIngressos(qtdSuperior, quantidade, ingressoEscolhido);

    } else if (ingressoEscolhido == cadeiraInferior) {
        // Subtrair a quantidade de ingressos
        subtrairIngressos(qtdInferior, quantidade, ingressoEscolhido);

    } else {
        alert('Tipo de ingresso inválido. Verifique e tente novamente!');
        return;
    }
}
