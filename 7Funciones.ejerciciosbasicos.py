"1. Escribe una función que reciba dos números y devuelva su suma."

def suma(num1, num2):
    suma = num1 + num2
    print(suma)
    return suma

suma(3,4)

"2. Crea una función que reciba una lista de números y devuelva la media."

lista = [1,2,3,4,5,4,4,5,6,7,7,8,8,6,5,4]

def media(lista):
    media = sum(lista)/len(lista)
    print(media)
    return media

media(lista)

"3. Escribe una función que determine si un número es par o impar."

def paroimpar(numero):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

paroimpar(5)

"4. Crea una función que reciba una cadena y devuelva la cadena invertida."

def cadenainvertida(cadena):
    reves = "".join(reversed(cadena))
    print(reves)
    return reves

cadenainvertida("Hola a todos")

"5. Escribe una función que reciba una lista y devuelva la lista sin duplicados"

numeros = [1,2,3,2,2,3,4,5,6,7,8,8,8,9,0]

def lista(lista):
    repes = set(lista)
    print(repes)
    return repes

lista(numeros)

"6. Crea una función que calcule el factorial de un número."

def factor(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    print("El factorial es " + str(factorial))

factor(12)

"7. Escribe una función que reciba un número y determine si es primo."

def primo(numero):
    es_primo = True
    if numero < 2:
        es_primo = False
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break

    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

primo(13)

"8. Crea una función que reciba una lista de números y devuelva el número más grande"

lista = [1,2,3,4,5,6,7,8,9,10,345,23,34,5,6]

def listanumeros(lista):
    grande = max(lista)
    print(grande)
    return grande

listanumeros(lista)

"9. Escribe una función que reciba una cadena y cuente cuántas vocales tiene."

def vocales(string):
    contador = 0
    for i in string:
        if "a" == i in string:
            contador += 1
        elif "e" == i in string:
            contador += 1
        elif "i" == i in string:
            contador += 1
        elif "o" == i in string:
            contador += 1
        elif "u" == i in string:
            contador += 1
    print(contador)


vocales("Hola a todos vamos alla, aprendemos Python")

"10. 10.Crea una función que reciba dos listas y devuelva una lista con los elementos comunes."

def comunes(l1, l2):
    lista_final = []
    for i in l1:
        if (i not in lista_final) and (i in l2):
            lista_final.append(i)
    return lista_final

numeritos = [1,2,3,4,5,6,7,8,9]
numerotes = [5,6,7,8,9,10,11,12]

print(comunes(numeritos, numerotes))