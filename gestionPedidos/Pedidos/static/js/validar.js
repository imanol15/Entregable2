function validarFormularioPrecio() {
  var precio = parseFloat(document.getElementById('id_precio').value);
  if (precio < 0 || isNaN(precio)) {
    document.getElementById('resultadoprecio').textContent = "El precio debe ser un número no negativo.";
    return false;
  } else {
    document.getElementById('resultadoprecio').textContent = "";
    return true;
    }
  }
  function ActualizarFormularioPrecio() {
    var precio = parseFloat(document.getElementById('id_precio').value);
    if (precio < 0 || isNaN(precio)) {
      document.getElementById('resultadoprecio').textContent = "El precio debe ser un número no negativo.";
      return false;
    } else {
      document.getElementById('resultadoprecio').textContent = "";
      return true;
    }
  }
  
  
  function validarFormularioPrecioTotal() {
    var precioTotal = parseFloat(document.getElementById('id_preciototal').value);
    if (precioTotal < 0 || isNaN(precioTotal)) {
      document.getElementById('resultprecio').textContent = "El precio total debe ser un número no negativo.";
      return false;
    } else {
      document.getElementById('resultprecio').textContent = "";
      return true;
    }
  }
  
  function ActualizarFormularioPrecioTotal() {
    var precioTotal = parseFloat(document.getElementById('id_preciototal').value);
    if (precioTotal < 0 || isNaN(precioTotal)) {
      document.getElementById('resultprecio').textContent = "El precio total debe ser un número no negativo.";
      return false;
    } else {
      document.getElementById('resultprecio').textContent = "";
      return true;
    }
  }
  
  function ActualizarFormularioCIF() {
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
  