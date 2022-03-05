#Calcular la etapa de la vida, según edad:

edad = int(input("Digite su edad: "))

if(edad >=0 and edad <=14):
   print("Niño") 
elif(edad >=15 and edad <=28):
   print("Joven")   
elif(edad >=28 and edad <=60):
   print("Adulto")  
else:    
   print("Adulto mayor")