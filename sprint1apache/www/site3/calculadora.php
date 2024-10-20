<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora PHP</title>
</head>
<body>
    <h1>Calculadora</h1>

    <!-- Formulario HTML -->
    <form method="POST" action="calculadora.php">
        <label for="numero1">Número 1:</label>
        <input type="number" name="numero1" id="numero1" required>
        <br><br>

        <label for="numero2">Número 2:</label>
        <input type="number" name="numero2" id="numero2" required>
        <br><br>

        <label for="operacion">Operación:</label>
        <select name="operacion" id="operacion" required>
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multiplicacion">Multiplicación</option>
            <option value="division">División</option>
        </select>
        <br><br>

        <input type="submit" value="Calcular">
    </form>

    <!-- Procesamiento del formulario en PHP -->
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $numero1 = $_POST['numero1'];
        $numero2 = $_POST['numero2'];
        $operacion = $_POST['operacion'];
        $resultado = 0;

        if (is_numeric($numero1) && is_numeric($numero2)) {
            switch ($operacion) {
                case 'suma':
                    $resultado = $numero1 + $numero2;
                    echo "<h2>Resultado: $numero1 + $numero2 = $resultado</h2>";
                    break;
                case 'resta':
                    $resultado = $numero1 - $numero2;
                    echo "<h2>Resultado: $numero1 - $numero2 = $resultado</h2>";
                    break;
                case 'multiplicacion':
                    $resultado = $numero1 * $numero2;
                    echo "<h2>Resultado: $numero1 * $numero2 = $resultado</h2>";
                    break;
                case 'division':
                    if ($numero2 != 0) {
                        $resultado = $numero1 / $numero2;
                        echo "<h2>Resultado: $numero1 / $numero2 = $resultado</h2>";
                    } else {
                        echo "<h2>Error: No se puede dividir por cero.</h2>";
                    }
                    break;
                default:
                    echo "<h2>Error: Operación no válida.</h2>";
                    break;
            }
        } else {
            echo "<h2>Error: Por favor, ingresa valores numéricos válidos.</h2>";
        }
    }
    ?>
</body>
</html>

