<?php

class Controller_login{
    public function login($data){
    
    $url = "http://crypto-note-ia:8000/api/login";
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
     return @file_get_contents($url, false, $context);
  
  }
}