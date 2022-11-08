#Servidor 
import socket 
import datetime
import time
import platform
import os
host="localhost"
port=8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("servidor en espera de conexiones nuevas")
active, addr = server.accept()

while True:
    recibido = active.recv(1024).decode(encoding="ascii", errors="ignore")
    #Palabra date
    print("Cliente: ", recibido)
    if (recibido == "date"):
         #hora y fecha
        f = time.localtime()
        e = time.asctime(f)
        enviar = e
        active.send(enviar.encode(encoding="ascii", errors="ignore"))

    #Palabra os
    elif (recibido == "os"):
        enviar = str(platform.system() + " " + platform.release() + ", " + platform.processor()) 
        active.send(enviar.encode(encoding="ascii",errors="ignore"))
    
    #Palabra ls
    elif (recibido == "ls"):
       enviar = str(os.listdir())
       active.send(enviar.encode(encoding="ascii",errors="ignore"))

    elif (recibido == "salir"):
        break
    else:
        enviar=input("Server: ")
        active.send(enviar.encode(encoding="ascii", errors="ignore"))

active.close()
