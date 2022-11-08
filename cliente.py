import socket

host = "localhost"
port = 8080
#crear objeto llamado socket1
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#recibe una tupla del host y el puerto 
socket1.connect((host,port))
print("inicializando cliente")
#creamos el bucle infinito para conexión
while True:
    #creamos la variable enviar y le pedimos que "espere" a que el cliente escriba 
    enviar = input("Cliente: ")
    if (enviar == "DATE"):
        print("date")
    elif (enviar == "os"):
        print("OS")
    elif (enviar == "ls"):
        print("LS")
    elif (enviar == "salir"):
        print("saliendo")
        break
    

    #utilizamos la primitiva send para enviar por medio del socket la información
    socket1.send(enviar.encode(encoding="ascii", errors="ignore"))
    #vamos a recibir la respuesta del lado del cliente
    recibido = socket1.recv(1024)
    print("Servidor: ", recibido.decode(encoding="ascii", errors="ignore"))
    
#cerramos la conexión
socket1.close()