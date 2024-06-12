let total = 0;

function adicionar() {
    // Recuperando os elementos
    let qtde = document.getElementById('quantidade').value;
    
    if (qtde == '' || qtde == 0) {
        alert('Quantidade do produto não pode ser este valor. Favor verifique!');
        return;
    }

    let produto = document.getElementById('produto').value;
    let nomeProduto = produto.split(' -')[0];
    let valorUnitario = parseFloat(produto.split('R$')[1]);
    let subtotal = valorUnitario * qtde;

    // Adicionando no carrinho
    let listaProdutos = document.getElementById('lista-produtos');
    listaProdutos.innerHTML += `<section class="carrinho__produtos__produto">
          <span class="texto-azul">${qtde}x</span> ${nomeProduto} <span class="texto-azul">R$${subtotal}</span>
        </section>`;    

    // Alterando o Total
    total += subtotal;
    let exibirTotal = document.getElementById('valor-total');
    exibirTotal.innerHTML = `R$${total}`;

    // Limpando o campo quantidade
    document.getElementById('quantidade').value = '';

}

function limpar() {
    total = 0;
    document.getElementById('valor-total').innerHTML = `R$0`;
    document.getElementById('lista-produtos').innerHTML = '';
}
