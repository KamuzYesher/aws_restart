
frase = input("Ingrese su frase: ")
letra = input("Ingrese la letra a contar: ")

rep = 0

for x in frase:
    if (x == letra):
        rep += 1
    
print("La letra",letra,"se repite",rep,"veces")