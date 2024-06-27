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