#Calcular la estación según un mes proporcionado por consola:1
mes = int(input("Ingrese un mes del año: "))

if(mes == 1 or mes == 2 or mes ==3 or mes ==12):
    print("Invierno")
elif(mes == 7 or mes == 8):
    print("Verano")
elif(mes == 9 or mes == 10 or mes == 11):
    print("Otoño")
elif(mes == 4 or mes == 5 or mes == 6):
    print("Primavera")
else:
    print("Ese mes no existe, por favor verifique")






