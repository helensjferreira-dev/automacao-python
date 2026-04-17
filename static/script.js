// Formulário Products
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");
  const tabelaBody = document.getElementById("listProducts");
  const resetButton = document.getElementById("resetTable");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    console.log("Formulário de produtos enviado!");

    const codigo = document.getElementById("codigo").value;
    const marca = document.getElementById("marca").value;
    const tipo = document.getElementById("tipo").value;
    const categoria = document.getElementById("categoria").value;
    const preco_unitario = document.getElementById("preco_unitario").value;
    const custo = document.getElementById("custo").value;
    const obs = document.getElementById("obs").value;

    const novaLinha = document.createElement("tr");
    novaLinha.innerHTML = `
      <td>${codigo}</td>
      <td>${marca}</td>
      <td>${tipo}</td>
      <td>${categoria}</td>
      <td>${preco_unitario}</td>
      <td>${custo}</td>
      <td>${obs}</td>
    `;

    tabelaBody.appendChild(novaLinha);
    form.reset();
  });

  // Botão separado para limpar a tabela
  resetButton.addEventListener("click", () => {
    tabelaBody.innerHTML = "";
    console.log("Tabela limpa!");
  });
});

// Formulário Login
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login");

  loginForm.addEventListener("submit", function (event) {
    event.preventDefault();
    console.log("Formulário de login enviado!");

    // Redireciona para a página de produtos
    window.location.href =
      "https://helensjferreira-dev.github.io/automacao-python/templates/products.html";

    loginForm.reset();
  });
});
