window.addEventListener('DOMContentLoaded', function() {
    var codigoReferenciaField = document.getElementById('id_componentes_codigo_referencia');
    var nombreModeloField = document.getElementById('nombremodeloField');
    var marcaField = document.getElementById('marcaField');

    if (codigoReferenciaField && nombreModeloField && marcaField) {
    codigoReferenciaField.addEventListener('change', function() {
      if (codigoReferenciaField.value !== '') {
        nombreModeloField.style.display = 'block';
      } else {
        nombreModeloField.style.display = 'none';
        marcaField.style.display = 'none';
      }
    });

    nombreModeloField.addEventListener('change', function() {
      if (nombreModeloField.value !== '') {
        marcaField.style.display = 'block';
      } else {
        marcaField.style.display = 'none';
      }
    });
  }
  });