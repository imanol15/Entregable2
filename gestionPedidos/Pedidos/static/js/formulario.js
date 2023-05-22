window.addEventListener('DOMContentLoaded', function() {
  var productoSolicitadoField = document.getElementById('id_producto_solicitado');
  var pedidoSolicitadoField = document.getElementById('pedidoSolicitadoField');
  var cantidadField = document.getElementById('cantidadField');

  if (productoSolicitadoField && pedidoSolicitadoField && cantidadField) {
    productoSolicitadoField.addEventListener('change', function() {
      if (productoSolicitadoField.value !== '') {
        pedidoSolicitadoField.style.display = 'block';
      } else {
        pedidoSolicitadoField.style.display = 'none';
        cantidadField.style.display = 'none';
      }
    });

    pedidoSolicitadoField.addEventListener('change', function() {
      if (pedidoSolicitadoField.value !== '') {
        cantidadField.style.display = 'block';
      } else {
        cantidadField.style.display = 'none';
      }
    });
  }
});
