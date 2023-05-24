function validarFormularioPrecio() {
    // Obtener el valor del campo precio
    var precio = parseFloat(document.getElementById('id_precio').value);
  
    // Comprobar si el precio es un número positivo
    if (precio <= 0 || isNaN(precio)) {
      document.getElementById('resultadoprecio').innerHTML = "El precio debe ser un número positivo.";
      return false;
    } else {
      document.getElementById('resultadoprecio').innerHTML = "";
      return true;
    }
  }
  
  function validarFormularioPrecioTotal() {
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
  
  function validarFormularioCIF() {
    // Obtener el valor del campo CIF
    var cif = document.getElementById('id_cif').value;
  
    // Comprobar el CIF
    cif = cif.toUpperCase(); // Convertir el CIF a mayúsculas
  
    // Comprobar la longitud del CIF
    if (cif.length !== 9) {
      document.getElementById('resultcif').innerHTML = "El CIF debe tener 9 caracteres.";
      return false;
    }
  
    // Comprobar la letra inicial del CIF
    var letraInicial = cif.charAt(0);
    if (!/[ABCDEFGHJKLMNPQRSUVW]/.test(letraInicial)) {
      document.getElementById('resultcif').innerHTML = "El CIF debe comenzar con una letra válida.";
      return false;
    }
  
    // Comprobar los dígitos del CIF
    var digitos = cif.substr(1, 7);
    if (!/^\d+$/.test(digitos)) {
      document.getElementById('resultcif').innerHTML = "Los caracteres 2 a 8 del CIF deben ser dígitos.";
      return false;
    }
  
    // Si el CIF es válido, limpiar el mensaje de error
    document.getElementById('resultcif').innerHTML = "";
    return true;
  }
  