#Crear una lista donde almacenar 5 sueldos y luego ordenarla
salaries = [1200,760,400,200]

for i in range(len(salaries)):
    for j in range(i,len(salaries)):
        if salaries[i] > salaries[j]:
            temporal_var = salaries[i]
            salaries[i] = salaries[j]
            salaries[j] = temporal_var
        
print(salaries)