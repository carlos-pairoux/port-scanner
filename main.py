import socket

ip = input("Ingresá la IP a escanear: ")
puerto_inicio = int(input("Puerto inicial: "))
puerto_final = int(input("Puerto final: "))

for puerto in range(puerto_inicio, puerto_final +1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Esto crea un socket. AF_INET significa que vamos a trabajar con direcciones IPv4
    # (el formato típico 192.168.1.1). SOCK_STREAM significa que usamos TCP,
    # que es el protocolo de conexión más común y el que usan la mayoría de los servicios.
    s.settimeout(1)
    # Esto le dice al socket que espere máximo 1 segundo por puerto
    # antes de considerarlo cerrado y pasar al siguiente. Si no se pone, 
    # el programa se puede quedar colgado esperando respuesta indefinidamente.
    resultado = s.connect_ex((ip, puerto))
    # Esto intenta conectarse a la IP y puerto específico. 
    # connect_ex devuelve un número — si devuelve 0 significa que la conexión fue exitosa, 
    # o sea el puerto está abierto. Cualquier otro número significa que falló, 
    # puerto cerrado. Y se guarda en la variable resultado.
    if resultado == 0:
        print(f"Puerto {puerto} -> ABIERTO")
    else:
        print(f"Puerto {puerto} -> CERRADO")
    s.close() # Se cierra el socket para liberar recursos.