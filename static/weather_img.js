var p = document.querySelector(".status-info");
var texto = p.textContent.trim();
var agora = new Date();
var hora = agora.getHours();

if (texto == "Chuva Intensa" || texto == "Chuva Muito Intensa") {
  $("#weather_img").attr("src", "static/images/chuva.png");
} else if (texto == "Tempestade") {
  $("#weather_img").attr("src", "static/images/tempestade.png");
} else if (texto == "Nevando") {
  $("#weather_img").attr("src", "static/images/neve.png");
}

if (hora >= 6 && hora < 18) {
  if (texto == "Céu Limpo") {
    $("#weather_img").attr("src", "static/images/sol.png");
  } else if (texto == "Chuva Leve" || texto == "Chuva Moderada") {
    $("#weather_img").attr("src", "static/images/dia_chuva.png");
  } else if (texto == "Nublado") {
    $("#weather_img").attr("src", "static/images/dia_nublado.png");
  }
} else {
  if (texto == "Céu Limpo") {
    $("#weather_img").attr("src", "static/images/lua.png");
  } else if (texto == "Chuva Leve" || texto == "Chuva Moderada") {
    $("#weather_img").attr("src", "static/images/note_chuva.png");
  } else if (texto == "Nublado") {
    $("#weather_img").attr("src", "static/images/noite_nublado.png");
  }
}
