echo "<h1>🚀 CryptoNote IA - Frontend PHP</h1>";

// 1. Probar conexión con la Base de Datos (Postgres)
$host = 'db_crypto'; // Nombre del servicio en docker-compose
$db   = 'cryptonote_db';
$user = 'admin';
$pass = 'secret';

try {
    $dsn = "pgsql:host=$host;port=5432;dbname=$db;";
    $pdo = new PDO($dsn, $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
    echo "<p style='color: green;'>✅ Conexión a PostgreSQL: Exitosa</p>";
} catch (PDOException $e) {
    echo "<p style='color: red;'>❌ Error en DB: " . $e->getMessage() . "</p>";
}

$python_url = 'http://crypto-note-ia:8000/'; // Nombre del servicio en docker-compose
$response = @file_get_contents($python_url);

if ($response !== false) {
    echo "<p style='color: green;'>✅ Conexión a Python IA: Exitosa</p>";
    echo "<pre>Respuesta de la IA: " . htmlspecialchars($response) . "</pre>";
} else {
    echo "<p style='color: orange;'>⚠️ El backend de Python no responde (¿está encendido?)</p>";
}

phpinfo(); // Esto te confirmará que PHP está corriendo bien
?>