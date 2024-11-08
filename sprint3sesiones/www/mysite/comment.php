<?php 
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
    <body>
        <?php

        session_start();
        $user_id_a_insertar = 'NULL';
        if (!empty($_SESSION['user_id'])) {
        $user_id_a_insertar = $_SESSION['user_id'];
        }

        $id_libro= $_POST['id'];
        $comentario=$_POST['new_comment'];
        
    $query = "INSERT INTO tComentarios(comentario, usuario_id, libro_id) VALUES 
    ('".$comentario."',".$user_id_a_insertar.",".$id_libro.")";


        mysqli_query($db,$query) or die('Error');

        echo "<p>Nuevo Comentario ";
        echo mysqli_insert_id($db);
        echo " añadido</p>";

        echo "<a href='/detail.php?id=".$id_libro."'>Volver</a>";
        mysqli_close($db);
        ?>
    </body>
</html>