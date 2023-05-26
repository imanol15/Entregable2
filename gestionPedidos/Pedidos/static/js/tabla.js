// Obtén una referencia a la tabla y al elemento donde se mostrará la fila nueva
const tablaComponentes = document.getElementById('tabla-componentes');
const filaNueva = document.getElementById('fila-nueva');
let detallesVisible = false; // Variable para controlar si los detalles están visibles o no

// Agrega el evento de clic a los botones de detalle
const buttons = document.getElementsByClassName('detail_button');
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', mostrarDetalles);
}

// Función para mostrar u ocultar los detalles en la fila nueva
function mostrarDetalles(event) {
    // Obtén la fila actual y los datos necesarios
    const filaActual = event.target.parentNode.parentNode;
    const id = filaActual.cells[0].innerText;

    // Si los detalles están visibles y se hace clic nuevamente en el mismo botón, oculta los detalles
    if (detallesVisible && filaActual === filaNueva.previousElementSibling) {
        filaNueva.style.display = 'none';
        detallesVisible = false;
        return;
    }

    // Realiza una llamada a la API de Django para obtener los detalles del componente por su ID
    fetch(`/api/componentes/${id}/`)
        .then(response => response.json())
        .then(data => {
            const codigoReferencia = data.codigo_referencia;
            const modelo = data.modelo;
            const marca = data.marca;

            // Actualiza la fila nueva con los detalles
            filaNueva.innerHTML = `
                <td>${id}</td>
                <td colspan="4">
                    <strong>Código Referencia:</strong> ${codigoReferencia}<br>
                    <strong>Modelo:</strong> ${modelo}<br>
                    <strong>Marca:</strong> ${marca}<br>
                </td>
            `;

            // Muestra la fila nueva debajo de la fila actual
            filaActual.insertAdjacentElement('afterend', filaNueva);
            filaNueva.style.display = 'table-row';
            detallesVisible = true;
        })
        .catch(error => {
            console.error('Error al cargar los detalles:', error);
        });
}