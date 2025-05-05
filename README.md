# PWD_RDR
##Aplicacion simple para saber si tu pass esta comprometida o no##

Visitanos en nuestro repositorio oficial https://github.com/irubikcube/PWD_RDR

Gracias por descargar nuestro password reader. Agradecemos sinceramente que haya elegido nuestra aplicación para sus necesidades. Este manual ha sido creado para guiarte y de esta manera aprovechar el máximo de las funcionalidades que posee nuetros lector de contraeñas. Desde ya, esperamos que esta aplicación sea de gran utilidad garatizar tu seguridad informatica. Desde ya, como equipo #IRCSOFT#, estamos agradecidos con tu preferencia. 

1. Descripción General
Este programa permite al usuario verificar si su contraseña ha sido comprometida previamente, consultando
un archivo de texto con contraseñas filtradas conocido como 'rockyou-50.txt'.

El archivo contiene una lista de contraseñas comúnmente utilizadas o filtradas en bases de datos públicas y que producto de su longitud, es de dificil revision.

La utilidad de este programa es educativa y puede servir como herramienta de concientización sobre la
seguridad digital.

2. Funcionalidades del Programa
- Leer el archivo local 'rockyou-50.txt' y almacenarlo como una lista de contraseñas.
- Solicitar al usuario el ingreso de una contraseña mediante un menú interactivo, la cual debe ser una contraseña que el usuario haya fijado y crea que se encuentra comprometida.
- Comparar la contraseña ingresada con las del archivo.
- Mostrar un mensaje si la contraseña fue encontrada ('Have I Been Pwned!!!') o no ('lerolerolero!!!!').
- Permitir al usuario repetir la verificación o salir del programa.

3. Cálculos Realizados
- Utiliza una búsqueda lineal en una lista para verificar si la contraseña ingresada existe.
- Este proceso implica comparar el valor ingresado contra cada elemento de la lista de contraseñas.

4. Instrucciones de Uso
Manual de Usuario - Verificador de Contraseñas
1. Asegúrate que los archivos 'funciones.py', 'main.py' y 'rockyou-50.txt' esten en la misma carpeta. 
2. Ejecuta el archivo 'main.py' desde tu terminal o entorno de desarrollo.
3. Aparecerá un menú con dos opciones: verificar una contraseña o salir.
4. Ingresa tu contraseña para verificar si está en la lista de contraseñas filtradas.
5. Observa el resultado e interpreta el mensaje mostrado.
6. Repite el proceso o selecciona salir.
