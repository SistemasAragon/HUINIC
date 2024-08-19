$('#formularioLogin').on('submit', function(event) {
    // Prevenir el envío del formulario
    event.preventDefault();
    const correoElectronico = $('#correo').val();
    const password = $('#password').val();
    var formData = {
        correo: correoElectronico,
        password: password
    }
    // Realiza una solicitud POST AJAX para ingresar los datos del servidor
    $.ajax({
        url: '/validarLogin/',
        method: 'POST',
        data: formData,
        success: function (data) {
            if(!data.success){
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: data.message,
                    confirmButtonText: 'Entendido'
                });
                $('#correo').val('');
                $('#password').val('');
            }
        }
    });

});