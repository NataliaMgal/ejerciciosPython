#importar librerias (recetas/codigos prefabricados)
import math

#Declaro el bucle/iteracion/repeticion/la vuelta/loop/ repetir algo...}

print("Pandequesos santarrosano")
print("****")
print("0. Digita 0 para salir")
print("1. Digita 1 para calcular la raiz cuadrada de un #")
print("2. digita 2 para calcular la potencia 2 de un #")
print("****")

opcion=1

while(opcion !=0 ):

   #Variable controladora
   opcion= int(input("Digita una opcion: "))

#Preguntar por la opcion
   if(opcion== 0):
      break
   elif(opcion==1):
     numero=int(input("digita un numero: "))
     raiz=math.sqrt(numero)
     print(f"la raiz de {numero} es {raiz}")
   elif(opcion==2):
     numero=int(input("digita un numero: "))
     potencia=math.pow(numero,2)
     print(f"la potencia de numero es {potencia}")
   else:
     print("digita una opcion correcta")
