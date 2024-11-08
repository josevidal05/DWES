<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
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
        <h1>Conexión establecida</h1>
        <?php
            // Lanzar una query
            $query = 'SELECT * FROM tLibros';
            $result= mysqli_query($db, $query) or die('Query error');
            
            // Recorrer el resultado
            while ($row = mysqli_fetch_array($result)) {
                echo $row['nombre'];
                
                echo '<br>';
                echo '<img src='.$row['url_imagen'].'>';
                
                echo '<br>';
                echo $row['autor'];
                
                echo '<br>';
                echo $row['año_publicacion'];
                
                echo '<br>';
                echo '<a href=/detail.php?id='.$row['id'].'>ver detalles</a>';
                
                echo '<br>';
                echo '<br>';


            }
            
            mysqli_close($db);
        ?>
        <a href="/logout.php">Logout</a>

    </body>
</html>
