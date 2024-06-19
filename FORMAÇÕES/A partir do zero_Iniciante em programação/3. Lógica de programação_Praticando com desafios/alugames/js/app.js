let jogosAlugados = 0;
function exibirQuantosJogosAlugados() {
    console.log(`Total de jogos alugados: ${jogosAlugados}`);
}

function alterarStatus(numero) {
    let propriedadeImg = document.getElementById(`game-${numero}`).querySelector("div");
    let propriedadeBtn = document.getElementById(`game-${numero}`).querySelector("a");
    let propriedadeNome = document.getElementById(`game-${numero}`).querySelector("p");
    
    if (propriedadeImg.classList.contains("dashboard__item__img--rented")) {

        if (confirm(`Você tem certeza que deseja devolver o jogo ${propriedadeNome.textContent}?`)) {
            propriedadeImg.classList.remove("dashboard__item__img--rented");
            propriedadeBtn.classList.remove("dashboard__item__button--return");
            propriedadeBtn.innerText = "Alugar";
            jogosAlugados--;
        }

    } else {
        propriedadeImg.classList.add("dashboard__item__img--rented");
        propriedadeBtn.classList.add("dashboard__item__button--return");
        propriedadeBtn.innerText = "Devolver";
        jogosAlugados++;
    }

    exibirQuantosJogosAlugados();
}