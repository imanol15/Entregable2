function validarFormulario() {
    // Obtener el valor del campo precio total
    var precioTotal = parseFloat(document.getElementById('id_preciototal').value);
    
    // Comprobar si el precio total es un número positivo
    if (precioTotal <= 0 || isNaN(precioTotal)) {
      document.getElementById('resultprecio').innerHTML = "El precio total debe ser un número positivo.";
      return false;
    } else {
      document.getElementById('resultprecio').innerHTML = "";
      return true;
    }
  }