function buscarEmail() {
    var email = document.getElementById("correo").value;
    var contra = document.getElementById("contraseña").value;

    // Realizar una petición AJAX a la URL de Django para buscar el email
    fetch("/buscar_email?email=" + email)
        .then(response => response.json())
        .then(data => {
            if (data.exists) {
                if (data.password === contra) {
                    sessionStorage.setItem("email", email);
                    sessionStorage.setItem("contraseña", contra);
                   // window.location.href = "indexlogueado.html";
                } else {
                    alert("Contraseña incorrecta");
                }
            } else {
                alert("Email no registrado");
            }
        })
        .catch(error => {
            console.error("Ocurrió un error al buscar el email", error);
            alert("Ocurrió un error al buscar el email");
        });
}
