function alterarStatus(numero) {
    let propriedadeImg = document.getElementById(`game-${numero}`).querySelector("div");
    let propriedadeBtn = document.getElementById(`game-${numero}`).querySelector("a");
    
    if (propriedadeImg.classList.contains("dashboard__item__img--rented")) {
        propriedadeImg.classList.remove("dashboard__item__img--rented");
        propriedadeBtn.classList.remove("dashboard__item__button--return");
        propriedadeBtn.innerText = "Alugar";
    } else {
        propriedadeImg.classList.add("dashboard__item__img--rented");
        propriedadeBtn.classList.add("dashboard__item__button--return");
        propriedadeBtn.innerText = "Devolver";
    }
}