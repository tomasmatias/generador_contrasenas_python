import random # se importa la libreria "random" que contiene variados numeros aleatorios.
import string # libreria "string" contiene caracteres alfanumericos para poder ser utilizados.

def generar_contrasena(longitud):

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range (longitud))
    return contrasena

longitud_deseada = int(input("Ingrese la longitud deseada para la contraseña "))
contrasena_generada = generar_contrasena (longitud_deseada)
print("contraseña generada", contrasena_generada)


