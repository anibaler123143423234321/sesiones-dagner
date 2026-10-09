// Sesión 14 · Al abrir el modal, el curso de la tarjeta queda elegido en el formulario.
// Bootstrap avisa con el evento show.bs.modal; relatedTarget es el botón que lo abrió.
const modalInscripcion = document.getElementById('inscripcion');
const selectCurso = document.getElementById('ins-curso');

modalInscripcion.addEventListener('show.bs.modal', (evento) => {
  const boton = evento.relatedTarget;
  if (boton && boton.dataset.curso) {
    selectCurso.value = boton.dataset.curso;
  }
});
