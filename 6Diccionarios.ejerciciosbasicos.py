"1. Crea un diccionario que represente a un estudiante (nombre, edad, curso) e imprime sus datos."

diccionario = {"Nombre": "Alvaro", "Edad": 16, "Curso": "1A"}

print(diccionario)

"2. Escribe un programa que pida al usuario una palabra y cuente la frecuencia de cada letra."

palabra = input("Dame una palabra: ")
letrasrepes = {}

contador = 0

for letra in palabra:
    if letra in letrasrepes:
        if letrasrepes[letra]:
            contador += 1
        letrasrepes[letra] += 1
    else:
        letrasrepes[letra] = 1

print(letrasrepes)

"3. Crea un diccionario que almacene los precios de tres productos y calcule el total."

dicciprecios = {"Patatas": 0.60, "Mangos": 1.20, "Arroz": 1.50}

print(sum(dicciprecios.values()))

"4. Escribe un programa que pida al usuario tres países y sus capitales, y los almacene en un diccionario."

pais1, pais2, pais3 = input("Dame tres paises").split(", ")
capital1, capital2, capital3 = input("Dame tres capitales").split(", ")

dicciopaises = {pais1: capital1, pais2: capital2, pais3: capital3}

print(dicciopaises)

"5. Crea un diccionario con tres elementos y luego añade un nuevo par clave-valor."

nuevodiccionario = {"Coco": "perro", "Raza": "Golden/Collie", "Edad": 2.5}

nuevodiccionario["Juguetes"] = "Pelotas, hinchables, huesos"

print(nuevodiccionario)

"6. Escribe un programa que reciba una cadena y cuente la frecuencia de cada palabra."

string = input("Dame una palabra: ")
letrasrepes = {}
contador = 0

for letra in string:
    if letra in letrasrepes:
        if letrasrepes[letra]:
            contador += 1
        letrasrepes[letra] += 1
    else:
        letrasrepes[letra] = 1

print(letrasrepes)

"7. Crea un diccionario que almacene las notas de tres estudiantes y calcule la nota media."

notas = {"Estudiante1": 7, "Estudiante2": 8, "Estudiante3": 9}

suma = sum(notas.values())
valores = len(notas.values())

media = suma / valores

print(media)

"8. Escribe un programa que reciba una lista de nombres y los almacene en un diccionario con su longitud."

nom1, nom2, nom3, nom4 = input("Dame cuatro nombres: ").split(", ")

nombres = {nom1: len(nom1), nom2: len(nom2), nom3: len(nom3), nom4: len(nom4)}

print(nombres)

"9. Crea un diccionario que almacene tres libros y sus autores, y luego imprímelo."

libros = {"El Señor de los Anillos": "JRR Tolkien", "Noches Blancas": "Fiodor Dostoievsky", "Don Quijote": "Miguel de Cervantes"}

print(libros)

"10. Escribe un programa que elimine una clave específica de un diccionario."

clave = {"Clave1": 1, "Clave2": 2, "Clave3": 3}

del clave["Clave1"]

print(clave)