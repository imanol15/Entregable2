function validarFormulario() {
  // Obtener el valor del campo precio 
  var precio = parseFloat(document.getElementById('id_precio').value);
  
  // Comprobar si el precio  es un número positivo
  if (precio <= 0 || isNaN(precio)) {
    document.getElementById('resultadoprecio').innerHTML = "El precio debe ser un número positivo.";
    return false;
  } else {
    document.getElementById('resultadoprecio').innerHTML = "";
    return true;
  }
}