
from funciones import leer_contraseñas, menu

if __name__ == "__main__":
    nombre_archivo = "rockyou-50.txt"
    contraseñas = leer_contraseñas(nombre_archivo)
    if contraseñas:
        menu(contraseñas)
