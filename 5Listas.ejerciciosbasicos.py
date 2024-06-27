import numpy

"1. Declara una lista con cinco números e imprime el número mayor"

lista = [1, 2, 8, 5, 7]

print(max(lista))

"2. Crea un programa que pida al usuario cinco números, los guarde en una lista y muestre la lista en orden inverso."

num1, num2, num3, num4, num5 = input("Introduce 5 numeros: ").split(" ")

lista = [num1, num2, num3, num4, num5]

for i in lista[::-1]:
    print(i)

"3. Escribe un programa que sume todos los elementos de una lista."

suma = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(suma))

"4. Crea un programa que multiplique todos los elementos de una lista."

multiplica = [3, 4, 5, 6, 7, 3, 4]

print(numpy.prod(multiplica))

"5. Escribe un programa que elimine los elementos duplicados de una lista."

repetidos = [1, 2, 3, 4, 5, 6, 3, 2, 2, 2, 1, 10]

resultado = set(repetidos)

print(resultado)

"6. Crea una lista con los números del 1 al 10 y luego imprime solo los números pares."

pares = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

for i in pares:
    if i % 2 == 0:
        print(i)

"7. Escribe un programa que encuentre el segundo número más grande en una lista."

segundogrande = [1, 2, 98, 34, 23, 122, 3324, 23, 44, 345, 450]

print(sorted(segundogrande)[-2])

"8. Crea un programa que cuente cuántas veces aparece un número dado en una lista."

numero = int(input("Introduce un numero: "))

lista2 = [1,2,1,1,2,3,4,6,4,5,4,5,8,9,6,5,4,4,3,2,2,6,7,5,6,6,6]
contador = 0

for i in lista2:
    if i == numero:
        contador += 1


print(f"El numero {numero} se encuentra repetido " + str(contador) + " veces.")

"9. Escribe un programa que combine dos listas en una sola."

nuevalista = [1,2,3,4,5,6,7,8,9,10]
viejalista = [11,12,13,14,15,16,17]

resultado = nuevalista + viejalista

print(resultado)

"10. Crea un programa que ordene una lista de números en orden ascendente."

ordenascendente = [1,2,5,6,8,3,4,7,9,10]

ordenada = sorted(ordenascendente)

print(ordenada)




