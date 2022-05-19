#este programa le pedira su nombre al usuario y se lo devolvera en mayusculas, minusculas y con la primera letra de cada palabra en mayuscula

nombre=input("Introduzca su nombre completo por favor: ")

nombre_lower=nombre.lower()
nombre_upper=nombre.upper()
nombre_title=nombre.title()

print(nombre_lower)
print(nombre_upper)
print(nombre_title)
