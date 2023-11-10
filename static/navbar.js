const list = document.querySelectorAll(".list");

/* Responsável por atribuir a classe "active" nos elementos HTML, para atualização
do estilo na barra de navegação. */
function activeLink() {
  list.forEach((item) => item.classList.remove("active"));
  this.classList.add("active");
}
list.forEach((item) => item.addEventListener("click", activeLink));
