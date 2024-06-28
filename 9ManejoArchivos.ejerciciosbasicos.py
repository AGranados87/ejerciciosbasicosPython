"1. Escribe un programa que cree un archivo, escriba ¡Hola, Mundo! en él y luego lo lea."

archivo = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/TEXTO.txt", "w")

archivo.writelines("Hola mundo! Estamos aprendiendo Python poco a poco.")

archivo.close()

archivo = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/TEXTO.txt", "r")

lectura = archivo.read()

print(lectura)

archivo.close()

"2. Crea un programa que lea un archivo de texto y cuente cuántas líneas tiene."

archivo2 = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/TEXTO1.txt", "w")

archivo2.writelines(["Hola a todos. Estamos aprendiendo Python.\n", "Esto es otra línea.\n", "Y una tercera."])

archivo2.close()

archivo2 = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/TEXTO1.txt", "r")

leer = archivo2.readlines()
contador = len(leer)

print(contador)

archivo2.close()

"3. Escribe un programa que lea un archivo de texto y cuente cuántas palabras tiene."

archivo3 = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/TEXTO1.txt", "r")

palabras = str(archivo3.readlines()).split(" ")

print(len(palabras))

"4. Crea un programa que lea un archivo de texto y lo imprima línea por línea."

archivo4 = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto2.txt", "w")

archivo4.writelines(["Hola a todos, perros.\n Otra linea,\n y otra mas"])

archivo4.close()

archivo4 = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto2.txt", "r")

print(archivo4.readline())
print(archivo4.readline())
print(archivo4.readline())

archivo4.close()

"5. Escribe un programa que añada una línea de texto al final de un archivo existente."

archivo4 = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto2.txt", "a+")

archivo4.write("\nOtra linea mas")

archivo4.close()

"6. Crea un programa que copie el contenido de un archivo a otro."

with (open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto2.txt", "r") as archivo1,
      open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto3.txt", "w") as archivoX):

    for line in archivo1:
        archivoX.writelines(line)

"7. Escribe un programa que lea un archivo y reemplace una palabra específica por otra."

archivoX = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto3.txt", "r+")

for l in archivoX:
    archivoX.write(l.replace("linea", "PATO"))

"8. Crea un programa que lea un archivo y lo imprima en orden inverso."

archivoZ = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto4.txt", "w")

archivoZ.writelines(["Vamos a comernos un coquete a la parrilla, estara genial"])

archivoZ.close()

with open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto4.txt", "r") as archivoZ:

    for linea in archivoZ:
        contenido = linea
        print("".join(reversed(contenido)))

"9. Crea un programa que lea un archivo y cuente cuántas veces aparece una palabra específica."

archivoR = open("C:/Users/agran/OneDrive/Escritorio/PRUEBAPYTHON/texto4.txt", "r")

for w in archivoR:
    contador = w.count("comernos")
print(contador)

archivoR.close()
