let amigos = [];

function adicionar() {
  let amigo = document.getElementById("nome-amigo");

  if (amigo.value === "") {
    alert("Necessário o nome do amigo antes de adicionar.");
    return;
  } else if (amigos.includes(amigo.value)) {
    alert("Não podem ter 2 nomes iguais na lista!");
    return;
  }

  let lista = document.getElementById("lista-amigos");

  amigos.push(amigo.value);

  if (lista.textContent == "") {
    lista.textContent = amigo.value;
  } else {
    lista.textContent =
      lista.textContent = `${lista.textContent}, ${amigo.value}`;
  }

  amigo.value = "";
  amigo.focus();
}

function sortear() {
  if (amigos.length < 2) {
    alert("É necessário ter pelo menos 2 amigos na lista!");
    return;
  }
  embaralhar(amigos);

  let sorteio = document.getElementById("lista-sorteio");
  for (let i = 0; i < amigos.length; i++) {
    if (i == amigos.length - 1) {
      sorteio.innerHTML =
        sorteio.innerHTML + amigos[i] + " --> " + amigos[0] + "<br/>";
    } else {
      sorteio.innerHTML =
        sorteio.innerHTML + amigos[i] + " --> " + amigos[i + 1] + "<br/>";
    }
  }
}

function embaralhar(lista) {
  for (let indice = lista.length; indice; indice--) {
    const indiceAleatorio = Math.floor(Math.random() * indice);
    [lista[indice - 1], lista[indiceAleatorio]] = [
      lista[indiceAleatorio],
      lista[indice - 1],
    ];
  }
}

function reiniciar() {
  amigos = [];
  document.getElementById("lista-amigos").innerHTML = "";
  document.getElementById("lista-sorteio").innerHTML = "";
}
