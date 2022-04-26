import socket #comando para traer la libreria.

IP = socket.gethostbyname (socket.gethostname()) #Las variables que quedan fijas van en mayuscula. #¨by name¨ selecciona la direccion ip. ¨name¨ selecciona el nombre del dispositivo.
PORT = 8000  #es un canal de comunicacion.
server = socket.socket ()  #primero llamo a la libreria socket, luego a la funcion socket.
server.bind ((IP,PORT)) #manda al servidor a la direccion ip indicada.
server.listen () #habilita al servidor para hacer conexiones.
print (f"server levantar en {IP}") #f significa para decir que vamos a introducir una variables
#cuando vamos a imprimir una variable, ponesmos {} para que ponga el valor de la variable.
conn, addr = server.accept ()  #conexion que recibe, es una conexion que acepta. Tambien bloquea la comunicacion. Por eso esta fuera del while
print (f"cliente conectado en {addr}")

while True:
    cuenta = conn.recv(1024) #cantidad de bits que puedo recibir de golpe
    cuenta = cuenta.decode('utf-8') #decodifico la variable
    cuenta = int(cuenta) #convierto el string en entero
    #cuenta_int = len (cuenta) #convierto lo decodificado en un entero
    msg = conn.recv(cuenta).decode('utf-8')
    print(f"Cliente dijo: {msg}")
    if msg == "close":
        break