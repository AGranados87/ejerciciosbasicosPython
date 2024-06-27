"1. Escribe un programa que imprima los números del 1 al 10."

for i in range(1, 11):
    print(i)

"2. Crea un programa que pida al usuario un número y muestre su tabla de multiplicar (del 1 al 10)."

numero = int(input("Introduce el numero: "))

for i in range(1, 11):
    resultado = numero * i
    print(resultado)

"3. Escribe un programa que imprima los números pares del 1 al 20."

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

"4. Crea un programa que imprima los números del 1 al 100 en orden inverso."

for i in reversed(range(1, 101)):
    print(i)

"5. Escribe un programa que pida al usuario un número y calcule su factorial."

numero = int(input("Introduce un numero: "))
factorial = 1
for i in range(1, numero + 1):
    factorial = factorial * i
print("El factorial es " + str(factorial))

"6. Crea un programa que sume todos los números del 1 al 50."

contador = 0
for i in range(1, 51):
    contador += i
    print(contador)

"7. Escribe un programa que pida al usuario 5 números y luego los imprima en orden inverso."

num1, num2, num3, num4, num5 = input("Introduce 5 numeros: ").split(" ")

lista = [num1, num2, num3, num4, num5]
for i in lista[::-1]:
    print(i)

"8. Crea un programa que pida al usuario una cadena y la imprima carácter por carácter."

string = input("Introduce un texto: ")

for i in string:
    print(i.split(" "))

"9. Escribe un programa que pida al usuario una cadena y cuente cuántas vocales tiene."

cadena = input("Escribe lo que quieras: ")

contador = 0

for i in cadena:
    if i == "a" in cadena:
        contador += 1
    elif i == "e" in cadena:
        contador += 1
    elif i == "i" in cadena:
        contador += 1
    elif i == "o" in cadena:
        contador += 1
    elif i == "u" in cadena:
        contador += 1
print("Numero de vocales: " + str(contador))

"10. Crea un programa que pida al usuario un número y determine si es primo."

numero = int(input("Introduce un numero y te dire si es primo: "))
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