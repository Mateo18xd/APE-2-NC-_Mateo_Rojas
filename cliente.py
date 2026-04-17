import time
import os

archivo_entrada = "comunicacion/entrada_servidor.txt"
archivo_salida = "comunicacion/salida_servidor.txt"

def cliente():
    print(" Cliente de Sistemas Distribuidos ")
    
    while True:
        mensaje = input("\nIngrese el mensaje para enviar (o 'salir'): ")
        if mensaje.lower() == 'salir':
            break

        
        with open(archivo_entrada, "w") as f:
            f.write(mensaje)
        
        print("Enviando mensaje...")
        time.sleep(2) 

        
        if os.path.exists(archivo_salida):
            with open(archivo_salida, "r") as f_res:
                respuesta = f_res.read()
                print(f"Resultado del servidor: {respuesta}") 
        else:
            print("Esperando respuesta del servidor...")

if __name__ == "__main__":
    cliente()