"""
Ejercicio 1: Adivina el número 🎯

Escribe un programa en Python que haga lo siguiente:

    1º Genere un número aleatorio entre 1 y 10.
    2º Pida al usuario que adivine el número.
    3º Compruebe la respuesta y muestre pistas:
    4º Si el número introducido es menor, indicar: "Es un número más alto."
    5º Si es mayor, indicar: "Es un número más bajo."
    6º Repetir hasta que el usuario acierte.""


from enum import IntEnum
import random
from tkinter import W

numero_secreto = random.randint(1, 10)
n_int = 0 

print ("Intenta adivinar el número:\n")
print ("Preparado....... YA!\n")

while True:
    int_usu = int(input("Introduce el número:"))
    n_int += 1 

    if int_usu < numero_secreto:
        print ("El número es más grande que ese")
    elif int_usu > numero_secreto:  
        print ("El número es más pequeño") 
    else:
        print ("El número es correcto ;)")
        break

"""

#Ejercicio 2: Calculadora de números pares.

"""
Escribe un programa en Python que:

    1º Pida al  usuario un número entero positivo.
    2º Compruebe si el número es válido (mayor que 0). Si no lo es, debe volver a pedirlo.
    3º Muestre todos los números pares desde 2 hasta el número ingresado (incluido si es par).
    4º Si el usuario introduce un número negativo o 0, el programa de seguir pidiendo un número válido.
 

print("Introduce un número entero mayor a 0")

while True:

    num_usu = int(input("Introduce el número: "))

    if num_usu <= 0: # Verificamos que el número sea mayor que 0
        print("El número introducido no es válido, vuelve a introducirlo.")

    else:
        print(f"Números pares hasta {num_usu}:")

        for i in range(2, num_usu + 1, 2):  # Generamos los números pares
            print(i)
        break  # Salimos del bucle cuando el número es válido
"""

"""
Ejercicio 1:
    -Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

Ejercicio 2
    -Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.    

Ejercicio 3
    -Escribir una función que reciba un número entero positivo y devuelva su factorial.   

Ejercicio 4
    -Escribir una función que calcule el total de una factura tras aplicarle el IVA.
    -La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
    -Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%. 

Ejercicio 5
    -Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.      

    
#Ejercicio 1: 

def saludo ():
    print("Hola amiga")

saludo()   


#Ejercicio 2: 


def sal_nom (nombre):
    print(f"hola {nombre}")

sal_nom("Pedro")    


#Ejercicio 3:
 
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

num = int(input("Introduce un número entero positivo: "))
print(f"El factorial de {num} es {factorial(num)}")

#Ejercicio 4: 

"""




