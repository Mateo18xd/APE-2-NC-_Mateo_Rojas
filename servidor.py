import time
import os

archivo_entrada = "comunicacion/entrada_servidor.txt"
archivo_salida = "comunicacion/salida_servidor.txt"

def servidor():
    print(" Servidor Activo (Simulación de Servicio) ")
    ultimo_mensaje = ""

    if not os.path.exists("comunicacion"):
        os.makedirs("comunicacion")
    
    open(archivo_entrada, 'a').close() 

    while True:
        try:
            with open(archivo_entrada, "r") as f:
                contenido = f.read().strip()

           
            if contenido and contenido != ultimo_mensaje:
                print(f"Mensaje recibido: {contenido}")
                
               
                resultado = contenido.upper()
                
               
                with open(archivo_salida, "w") as f_out:
                    f_out.write(resultado)
                
                ultimo_mensaje = contenido
                print(f"Respuesta enviada: {resultado}")
            
            time.sleep(1) 
            
        except Exception as e:
            print(f"Error en el servidor: {e}")
            time.sleep(1)

if __name__ == "__main__":
    servidor()