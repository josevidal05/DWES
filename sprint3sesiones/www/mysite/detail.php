<?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');


    if (!isset($_GET['id'])) {
        die('No se ha especificado un libro');
    }


    $libro_id = $_GET['id'];
    $query = 'SELECT * FROM tLibros WHERE id=' . $libro_id;
    $result = mysqli_query($db, $query) or die('Query error');
    $libro = mysqli_fetch_array($result);

    if(!$libro){
        die('El libro no existe');
    }
?>

<html>
    <head>
        <style>
            img{
                width: 100px;
                height: 100px;
            }
        </style>
    </head>
    
    <body>
        <h1>Detalles del libro</h1>
        <div class="detalle-libro">
            <h2><?php echo $libro['nombre']; ?></h2> 
            <img src=" <?php echo $libro['url_imagen']; ?>"> 

        </div>

        <h3>Comentarios:</h3>
        <ul class="comentarios">

            <?php
                $query2 = 'SELECT * FROM tComentarios WHERE libro_id=' . $libro_id;
                $result2 = mysqli_query($db, $query2) or die('Error en la consulta de comentarios');

                while ($comentario = mysqli_fetch_array($result2)) {
                echo '<li>' . $comentario['comentario'] . '</li>';
                echo '<p>Fecha del comentario: ';
                echo $comentario['fecha'].'</p>';

            }
            ?>
        </ul>
        <!--Creamos un forms  donde permitimos añadir comentarios, al hacer submit nos redirigirá a comment.php-->
        <p>Deja un nuevo comentario</p>
        <form action="/comment.php" method="post">
            <textarea rows="4" cols="50" name="new_comment"></textarea><br>
            <input type="hidden" name="id" value="<?php echo $libro_id; ?>">
            <input type="submit"  value="Comentar">
        </form>

        <a href="/logout.php">Logout</a>
        
        <?php 
            mysqli_close($db);
        ?>
    </body>
</html>