"1. 1. Escribe un programa que pida al usuario su nombre y lo imprima en mayúsculas."

nombre = input("Dime tu nombre: ")

print(nombre.upper())

"2. Crea un programa que pida una frase al usuario y cuente cuántas palabras tiene."

cadena = input("Introduce un texto: ")

numeros = len(cadena.split(" "))

print(numeros)

"3. Escribe un programa que pida al usuario una cadena y determine si es un palíndromo."

palindromo = input("Introduce un texto: ")

reves = "".join(reversed(palindromo))

if palindromo == reves:
    print(f"{palindromo} es un palindromo.")
else:
    print(f"{palindromo} no es un palindromo.")

"4. Crea un programa que reemplace todas las vocales de una cadena por asteriscos."

asteriscos = "El Señor de los Anillos"

vocal1 = asteriscos.replace("a", "*")
vocal2 = vocal1.replace("e", "*")
vocal3 = vocal2.replace("i", "*")
vocal4 = vocal3.replace("o", "*")
vocal5 = vocal4.replace("u", "*")

print(vocal5)

"5. Escribe un programa que cuente cuántas veces aparece una letra en una cadena."

texto = "Vamos a aprender Python haciendo ejercicios poco a poco."
letras = {}
contador = 0

for l in texto:
    if l in letras:
        if letras[l]:
            contador += 1
        letras[l] += 1
    else:
        letras[l] = 1

print(letras)

"6. Crea un programa que pida al usuario una cadena y la imprima en orden inverso."

txt = input("Escribe lo que quieras: ")

texto1 = " ".join(reversed(txt))

print(texto1)

"7. Escribe un programa que separe una cadena en palabras y las almacene en una lista."

chain = "Vamos a aprender Python de verdad mediante ejercicios."
palabritas = []

separado = chain.split(" ")

palabritas.append(separado)

print(palabritas)

"8. Crea un programa que pida al usuario dos cadenas y determine si son anagramas."

cadena1 = input("Introduce una cadena: ")
cadena2 = input("Introduce otra cadena de texto: ")

if len(cadena1) != len(cadena2):
    print("No puede ser un anagrama.")

def anagramaSolucion2(cadena1,cadena2):
    unaLista1 = list(cadena1)
    unaLista2 = list(cadena2)

    unaLista1.sort()
    unaLista2.sort()

    pos = 0
    coincide = True

    while pos < len(cadena1) and coincide:
        if unaLista1[pos]==unaLista2[pos]:
            pos = pos + 1
        else:
            coincide = False

    return coincide

print(anagramaSolucion2(cadena1, cadena2))


"9. Escribe un programa que elimine los espacios en blanco de una cadena."

blanco = "Estamos aprendiendo el manejo de cadenas en Python. Aqui eliminamos los espacios en blanco.".replace(" ","")

print(blanco)

"10. Crea un programa que pida al usuario una cadena y la imprima sin las vocales."

novocales = input("Introduce una frase: ")

v1 = novocales.replace("a", "")
v2 = v1.replace("e", "")
v3 = v2.replace("i", "")
v4 = v3.replace("o", "")
v5 = v4.replace("u", "")

print(v5)












