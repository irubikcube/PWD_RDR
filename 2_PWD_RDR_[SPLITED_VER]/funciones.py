
def leer_contraseñas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8', errors='ignore') as archivo:
            contraseñas = [linea.strip() for linea in archivo.readlines()]
        return contraseñas
    except FileNotFoundError:
        print("El archivo no fue encontrado. Asegúrate de que 'rockyou-50.txt' esté en la misma carpeta del script.")
        return []

def menu(contraseñas):
    while True:
        print("\n--- MENÚ ---")
        print("1. Verificar contraseña")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            password = input("Ingresa tu contraseña: ")
            if password in contraseñas:
                print("Have I Been Pwned!!!")
            else:
                print("lerolerolero!!!!")
        elif opcion == '2':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
