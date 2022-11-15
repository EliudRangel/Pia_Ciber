$ip = "192.168.0.1"
$puertos = @(1..500)

foreach($p in $puertos){
#Creo objeto TcpClient
    $TCPObject = New-Object System.Net.Sockets.TcpClient
    try{
        $resultado = $TCPObject.ConnectAsync($ip, $p).Wait(100)
    }
    catch{
    }
    
    if ($resultado -eq "True")
    {
        Write-Host "El puerto"  $p  "Esta abierto"
    }
}
$TCPObject.Close()