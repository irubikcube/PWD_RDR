
def leer_contraseñas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8', errors='ignore') as archivo:
            contraseñas = [linea.strip() for linea in archivo.readlines()]
        return contraseñas
    except FileNotFoundError:
        print("El archivo no fue encontrado. Asegúrate de que 'rockyou-50.txt' esté en la misma carpeta de la app.")
        return []


def menu(contraseñas):
    while True:
        print("\n--- MENÚ ---")
        print("1. Verificar mi Password")
        print("2. Sacame de aquí")
        opcion = input("Que quieres hacer?")

        if opcion == '1':
            password = input("Pon tu contraseña: ")
            if password in contraseñas:
                print("Have I Been Pwned!!!")
            else:
                print("lerolerolero!!!!")
        elif opcion == '2':
            print("¡Gracias por usar PWD_RDR, hasta luego!")
            break
        else:
            print("Nop, Intenta de nuevo.")
