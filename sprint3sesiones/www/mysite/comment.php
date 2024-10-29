<?php 
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
    <body>
        <?php
        $id_libro= $_POST['id'];
        $comentario=$_POST['new_comment'];

        

        
    $query = "INSERT INTO tComentarios(comentario, libro_id) VALUES 
    ('".$comentario."', ".$id_libro.")";


        mysqli_query($db,$query) or die('Error');

        echo "<p>Nuevo Comentario ";
        echo mysqli_insert_id($db);
        echo " añadido</p>";

        echo "<a href='/detail.php?id=".$id_libro."'>Volver</a>";
        mysqli_close($db);
        ?>
    </body>
</html>