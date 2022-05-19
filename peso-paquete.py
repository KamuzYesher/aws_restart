#Este programa calculara el peso del paquete basado en cuantos payasos y cuantas munecas lleva

ppayasos=112
pmunecas=75

numpay= int(input("¿Cuantos payasos van en el paquete? "))
nummune=int(input("¿Cuantas muñecas van en el paquete? "))

print("El peso del paquete es de", (numpay*ppayasos+nummune*pmunecas), "gramos" )