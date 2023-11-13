var toggleSwitch = document.getElementById("switch");
let elementos = document.querySelectorAll(".text");
let icons = document.querySelectorAll(".icon");

toggleSwitch.addEventListener("change", function () {
  if (this.checked) {
    document.body.classList.add("darkmode");
    for (let i = 0; i < elementos.length; i++) {
      elementos[i].classList.add("dark-btn");
    }
    for (let i = 0; i < icons.length; i++) {
      icons[i].classList.add("dark-txt");
    }
  } else {
    document.body.classList.remove("darkmode");
    for (let i = 0; i < elementos.length; i++) {
      elementos[i].classList.remove("dark-btn");
    }
    for (let i = 0; i < icons.length; i++) {
      icons[i].classList.remove("dark-txt");
    }
  }
});
