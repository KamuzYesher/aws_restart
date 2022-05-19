
subjects_list = []
score_list = []
num_subjects = int(input("Ingrese el numero de materias: "))

count=0
while count < num_subjects :
    subjects_list.append(input("Ingrese el nombre de la materia: "))
    score_list.append(input("Ingrese su calificacion: "))
    count +=1

i = 0
j = 0
while i < num_subjects :
    print("Yo estudie la materia de",subjects_list[i],'y he sacado', score_list[j]) 
    i +=1
    j +=1
#print(subjects_list)
#print(score_list)
