// Capturar los datos del formulario
document.getElementById("datos").addEventListener("submit", function(event) {
    event.preventDefault(); 
    
    // Obtener los valores del correo y contraseña
    var email = document.getElementById("correo").value;
    var password = document.getElementById("pass").value;
    
    // Verificar los datos
    if (email === "admin@patitas.com" && password === "admin12345") {
      window.location.href = 'adminPage'; // Redirigir
    } else {
      alert("Correo o contraseña incorrectos. Inténtalo de nuevo.");
    }
});