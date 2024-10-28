<?php
// Conexión a la base de datos
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<?php
// Verificar si se ha especificado el ID del juego
if (!isset($_GET['id'])) {
    die('No se ha especificado un libro');
}
$libro_id = $_GET['id'];

// Consulta para obtener los detalles del juego
$query = 'SELECT * FROM tLibros WHERE id=' . $libro_id;
$result = mysqli_query($db, $query) or die('Query error');
$only_row = mysqli_fetch_array($result);

// Mostrar los detalles del juego
echo '<h1>' . htmlspecialchars($only_row['nombre']) . '</h1>';
echo '<img src="' . htmlspecialchars($only_row['url_imagen']) . '" alt="Imagen del juego" style="width:200px;">';
echo '<h2>Autor: ' . htmlspecialchars($only_row['autor']) . '</h2>';
echo '<h3>Año de publicación: ' . htmlspecialchars($only_row['año_publicacion']) . '</h3>';
?>
<h3>Comentarios:</h3>
<ul>
<?php
// Consulta para obtener los comentarios asociados al juego
$query2 = 'SELECT c.comentario, u.nombre, u.apellidos 
           FROM tComentarios c 
           JOIN tUsuarios u ON c.usuario_id = u.id 
           WHERE c.libro_id=' . $libro_id;
$result2 = mysqli_query($db, $query2) or die('Query error');

// Mostrar los comentarios
while ($row = mysqli_fetch_array($result2)) {
    echo '<li><strong>' . htmlspecialchars($row['nombre']) . ' ' . htmlspecialchars($row['apellidos']) . ':</strong> ' . htmlspecialchars($row['comentario']) . '</li>';
}

// Cerrar la conexión a la base de datos
mysqli_close($db);
?>
</ul>
</body>
</html>

