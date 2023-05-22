document.addEventListener('DOMContentLoaded', function() {
  var aumentarBtn = document.getElementById('aumentar-btn');
  var disminuirBtn = document.getElementById('disminuir-btn');

  if (aumentarBtn && disminuirBtn) {
    aumentarBtn.addEventListener('click', function() {
      cambiarTamanioTexto(1.2);
    });

    disminuirBtn.addEventListener('click', function() {
      cambiarTamanioTexto(0.8);
    });
  }
});

function cambiarTamanioTexto(factor) {
  var elementosTexto = document.querySelectorAll('h1, h2, button, p, tr, td, th, a');

  elementosTexto.forEach(function(elemento) {
    var tamañoActual = parseInt(window.getComputedStyle(elemento).fontSize);
    var nuevoTamaño = tamañoActual * factor;

    elemento.style.fontSize = nuevoTamaño + 'px';
  });
}
