<?php

class Controller_ask{    
    public function ask($data){
    $url = "http://crypto-note-ia:8000/api/ask";
    $body = json_encode($data);

    #se puede poner globar y asi pasarlo como una variable  
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
     return @file_get_contents($url, false, $context);
  }
}
