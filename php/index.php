<?php

header('Access-Control-Allow-Origin: http://localhost:5173');
header('Content-Type: application/json');
header("Access-Control-Allow-Credentials: true");
header("Access-Control-Allow-Headers: Content-Type");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS, PUT, DELETE");
header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");

if($_SERVER['REQUEST_METHOD'] == 'OPTIONS') exit;
$request = trim($_SERVER['REQUEST_URI'], '/');
$path = explode('/', $request);
$router = $path[0];


$json_input = json_decode(file_get_contents('php://input'), true);

if (empty($json_input)){
 $dato = [
        "status" => "error",
        "message" => "No data received"
    ];
 
    echo json_encode($dato);
    exit();
}

switch ($router) {
    case 'login':
        require_once __DIR__ . '/controller/Login.php';
        $controller = new Controller_login();
        echo $controller-> login($json_input);
        break;

    case 'sing_up':
        require_once __DIR__ . '/controller/Sing_login.php';
        $controller = new Controller_Sing_Login();
        echo $controller->sing_login($json_input);
        break;

    case 'ask':
        require_once __DIR__ . '/controller/Ask.php';
        $controller = new Controller_ask();
        echo $controller->ask($json_input);
        break;


    default:
        http_response_code(404);
        echo json_encode(["error" => "Ruta '$router' no encontrada"]);
        break;
}

?>

