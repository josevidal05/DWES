<?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    $email = $_POST['f_email'];
    $password = $_POST['f_password'];
    $password2 = $_POST['f_password2'];
    //encriptamos la contraseña
    $contraseña_cifrada($password, PASSWORD_DEFAULT);

    $query = "SELECT email FROM tUsuarios WHERE email = '".$email."'";
    $result = mysqli_query($db, $query) or die('Query error');
    
    /*comprobamos que no haya campos vacios*/
    if ($email != "" && $password != "" && $password2!="") {
        /*Comprobamos que las dos contraseñas coincidan*/
        if ($password == $password2){
            if ($query == 0) {
                $consulta= $db->prepare("INSERT INTO tUsarios (email, contraseña) VALUES (?, ?)");
                $consulta->bind_param('ss', $email, $contraseña_cifrada);
                //$_SESSION['user_id'] = $only_row[0];
                //header('Location: main.php');
                if ($consulta->execute()){
                    header('Location: main.php');
                    exit();
                }else{
                    die('Error: no se pudo completar el registro');
                }

                $consulta-> close();
                $db-> close();

            } else {
                echo '<p>El usuario ya existe</p>';
            }
        } else{
            echo '<p>Las contraseñas no coinciden</p>';
        }
        
    } else {
        echo '<p>Correo y/o contraseña vacios</p>';
    }
?>  

