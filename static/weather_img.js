var p = document.querySelector(".status-info");
var texto = p.textContent.trim();
var agora = new Date();
var hora = agora.getHours();

// Altera a imagem da homepage baseado no clima atual
if (texto == "Chuva Intensa" || texto == "Chuva Muito Intensa") {
  $("#weather_img").attr("src", "static/images/chuva.png");
} else if (texto == "Tempestade") {
  $("#weather_img").attr("src", "static/images/tempestade.png");
} else if (texto == "Nevando") {
  $("#weather_img").attr("src", "static/images/neve.png");
}

// Verificação do horário do dia para exibir a imagem correta, sol ou lua.
// Se o horário estiver entre 06:00 e 18:00, ele mostra o sol.
if (hora >= 6 && hora < 18) {
  if (texto == "Céu Limpo") {
    $("#weather_img").attr("src", "static/images/sol.png");
  } else if (texto == "Chuva Leve" || texto == "Chuva Moderada") {
    $("#weather_img").attr("src", "static/images/dia_chuva.png");
  } else if (texto == "Nublado") {
    $("#weather_img").attr("src", "static/images/dia_nublado.png");
  }
  // Se estiver entre 18:01 e 5:59 ele mostra lua.
} else {
  if (texto == "Céu Limpo") {
    $("#weather_img").attr("src", "static/images/lua.png");
  } else if (texto == "Chuva Leve" || texto == "Chuva Moderada") {
    $("#weather_img").attr("src", "static/images/note_chuva.png");
  } else if (texto == "Nublado") {
    $("#weather_img").attr("src", "static/images/noite_nublado.png");
  }
}
