function validarFormulario() {
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
  
    document.getElementById('resultcif').innerHTML = "";
    return true;
  }