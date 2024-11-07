<?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    
    // Obtener datos del formulario
    $email_posted = $_POST['f_email'];
    $password_posted = $_POST['f_password'];
    
    // Consulta para verificar si el correo existe en la base de datos
    $query = "SELECT id, contraseña FROM tUsuarios WHERE email = '".$email_posted."'";
    $result = mysqli_query($db, $query) or die('Query error');
    
    if (mysqli_num_rows($result) > 0) {
        $only_row = mysqli_fetch_array($result);
        
        if (password_verify($password_posted, $only_row['contraseña'])) {
            // Contraseña correcta: iniciar sesión y redirigir
            session_start();
            $_SESSION['user_id'] = $only_row['id'];
            header('Location: main.php');
            exit;

        /*if ($only_row[1] == $password_posted) {
            session_start();
            $_SESSION['user_id'] = $only_row[0];
            header('Location: main.php');*/
        } else {
            echo '<p>Contraseña incorrecta</p>';
        }
    } else {
        echo '<p>Usuario no encontrado con ese email</p>';
    }
    // Cerrar la conexión a la base de datos
    mysqli_close($db);
?>