### Funciones  ###

#def palabra reservada para hacer funciones
# estructura es def nomFun (parámetros) : . 

from pydoc import text
import re


def my_function ():
    print("Esto es una función")

#Llamamos a la función.
my_function()

def sum_num (n1, n2) : 
    print (n1 + n2)

sum_num(5,7)    
sum_num(123,123)


def sum_num_retorno (n1, n2) : 
    return n1 + n2 

#Recordar que hay que asignar lo que nos devuelve la función a una variable y luego la llamamos para mostrarlo.
resultado = sum_num_retorno(10, 5)
print (resultado)

#Con la f accedemos a los valores de la fucnión.
def print_name (name, surname) : 
    print(f"{name} {surname}")

print_name("Jesús", "Jesús")


def print_name_with_default (name, surname, alias = "Sin alias") : 
    print(f"{name} {surname} {alias}")

print_name_with_default ("Peter", "Parker", "Spiderman")

#Con el * le decimos que de ese tipo de dato le podemos pasar los que queramos.
def mostrar_textos(*text) : 
    print(text)

mostrar_textos("Hola", "Pythone", "Peter")
mostrar_textos("Hola Mundo")

#Lo de upper es para mostrar todo en Mayúsculas.
def mostrar_texto(*text) : 
    for tex in text:
        print(tex.upper())

mostrar_texto("Hola", "Pythone", "Peter")






