<?php

header('Access-Control-Allow-Origin: http://localhost:5173');
header('Content-Type: application/json');
header("Access-Control-Allow-Credentials: true");
header("Access-Control-Allow-Headers: Content-Type");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS, PUT, DELETE");
header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");

class PythonConnection {
 private $url;
   
  public function __construct($endpoit){
     $this->url=$endpoit;
  }
  
  public function sudmin($data){
    $body = json_encode($data);

    $opts = [
    "http" => [
        "method" => "POST",
        "header" => "Accept: application/json\r\n" . "Content-Type: application/json\r\n",
        "content" => $body,
        "ignore_errors" => true,
        "timeout" => 10
    ]
   ];
   
   $context = stream_context_create($opts);
    return @file_get_contents($this->url, false, $context);
  }
}

$json_input = json_decode(file_get_contents('php://input'), true);
$new_connection = new PythonConnection("http://crypto-note-ia:8000/api/login");
echo $new_connection->sudmin($json_input);



// if (empty($json_data)) {
//     $dato = [
//         "status" => "error",
//         "message" => "No data received"
//     ];
 
//     echo json_encode($dato);
//     exit();
// }


// $url = "http://crypto-note-ia:8000/api/login";


// $opts = [
//     "http" => [
//         "method" => "POST",
//         "header" => "Accept: application/json\r\n" . 
//                     "Content-Type: application/json\r\n",
//         "content" => $data,
//         "ignore_errors" => true,
//         "timeout" => 10
//     ]
// ];

// $context = stream_context_create($opts);
// $response = @file_get_contents($url, false, $context);

// if ($response === false) {
    
//     $error = error_get_last();
//     echo $error['message'];

// } else {
    
//     $response_python = json_decode($response, true);
    
//     if (json_last_error() !== JSON_ERROR_NONE) {
//         echo "JSON decode error: " . json_last_error_msg();
//         exit;
   
//     } else {

//         $dato = [
//             "status" => "success",
//             "message" => $response_python
//         ];

//         echo json_encode($dato);
//         exit();
//     }
// }

?>

