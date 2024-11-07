<?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    
    //obetenemos los datos del formulario
    $email = $_POST['f_email'];
    $password = $_POST['f_password'];
    $password2 = $_POST['f_password2'];
    //encriptamos la contraseña
    //$contraseña_cifrada($password, PASSWORD_DEFAULT);
    if ($conn->connect_error) {
        die("Conexión fallida: " . $conn->connect_error);
    }
    
    // Verificar si se enviaron todos los datos del formulario
    if (!isset($_POST['f_email'], $_POST['f_password'], $_POST['f_password2'])) {
        echo "Todos los campos son obligatorios.";
        exit;
    }

    
    // Verificar si algún campo está vacío
    if (empty($email) || empty($password) || empty($password2)) {
        echo "Todos los campos son obligatorios.";
        exit;
    }
    
    // Verificar si las contraseñas coinciden
    if ($password !== $password2) {
        echo "Las contraseñas no coinciden.";
        exit;
    }
    
    // Comprobar si el correo ya existe en la base de datos
    $query= "SELECT * FROM tUsuarios where email = '$email'";
    $result = mysqli_query($db, $query);

    if (mysqli_num_rows($result)>0){
        echo "El correo electrónico ya está registrado";
        exit;
    }
    
    // Cifrar la contraseña
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);
    
    // Insertar el usuario en la base de datos
    $query = "INSERT INTO tUsuarios (nombre, apellidos, email, contraseña) VALUES
    ('', '', '$email', '$hashed_password')";
    
    if (mysqli_query($db, $query)) {
        // Redirigir a la página principal
        echo "El correo electrónico se ha registrado con exito";
        exit;
    } else {
        echo "Error al registrar el usuario: " . mysqli_error($db);
    }
    
    mysqli_close($db);
?>
