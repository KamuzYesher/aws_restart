#este programa pedira un nombre y cuantas veces se repetira en pantalla

nombre = input("Introduzca su nombre ") 
rep = int(input("Cuantas veces quiere que se repita "))

count = 0
while count < rep:
    print(nombre)
    count += 1