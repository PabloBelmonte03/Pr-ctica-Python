### Class ###

#Palabra reservada es class.
#pass es para cuando necesitamos algo que no se ejecute.
#En el nombre de las clases no hay restricciones de mayus.

class MyEmptyPerson:
    pass 

print (MyEmptyPerson)

#Estamos definiendo la clase y sus campos (constructor de clase).
class Person: 
    def __init__(self, name, surname):
        self.name = name #Asignamos las propiedades.
        self.surname = surname 


my_person = Person("Peter", "Parker")
print(f"{my_person.name} {my_person.surname}")


#Es lo mismo de arriba pero juntamos los parámetros. 
class Persona: 
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def caminar(self):
        print(f"{self.full_name} Está caminando")    
      
my_persona = Persona("Peter", "Parker")
print(my_persona.full_name)
my_persona.caminar()










