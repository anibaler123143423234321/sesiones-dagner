/* ==========================================================
   reproductor.js · Controles personalizados del video
   Sesión 07 · Elementos multimedia avanzados
   ========================================================== */

// 1. Guardamos en variables los elementos que vamos a usar
const video = document.getElementById("video-presentacion");
const controles = document.getElementById("controles-video");
const btnReproducir = document.getElementById("btn-reproducir");
const btnSilenciar = document.getElementById("btn-silenciar");
const barra = document.getElementById("barra-progreso");
const tiempo = document.getElementById("tiempo");

// 2. Quitamos los controles del navegador y mostramos los nuestros.
//    Si este archivo no carga, el video conserva sus controles nativos.
video.removeAttribute("controls");
controles.hidden = false;

// 3. Botón Reproducir / Pausar
btnReproducir.addEventListener("click", () => {
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
});

video.addEventListener("play", () => {
  btnReproducir.textContent = "Pausar";
});

video.addEventListener("pause", () => {
  btnReproducir.textContent = "Reproducir";
});

// 4. Botón Silenciar
btnSilenciar.addEventListener("click", () => {
  video.muted = !video.muted;
  btnSilenciar.textContent = video.muted ? "Activar sonido" : "Silenciar";
  btnSilenciar.setAttribute("aria-pressed", video.muted);
});

// 5. Barra de avance y contador de tiempo
function formatearTiempo(segundos) {
  const minutos = Math.floor(segundos / 60);
  const resto = Math.floor(segundos % 60);
  return minutos + ":" + String(resto).padStart(2, "0");
}

function actualizarAvance() {
  const duracion = video.duration || 0;
  barra.max = duracion;
  barra.value = video.currentTime;
  tiempo.textContent =
    formatearTiempo(video.currentTime) + " / " + formatearTiempo(duracion);
}

video.addEventListener("loadedmetadata", actualizarAvance);
video.addEventListener("timeupdate", actualizarAvance);
actualizarAvance();

// 6. Al mover la barra, el video salta a ese punto
barra.addEventListener("input", () => {
  video.currentTime = barra.value;
});
