#Este programa calcula el indice de masa corporal pidiendo al usuario su peso y estatura

peso= float(input("Porfavor introduzca su peso en Kilogramos: "))
altura= float(input("Porfavor introduzca su altura en Metros: "))

imc= round(peso/altura,2)

print("Tu índice de masa corporal es",imc)
