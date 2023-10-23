#EJERCICIO5
curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for x in curso.keys():
    print(x+" tiene "+str(curso[x]),"créditos")
    total_creditos += curso[x]
print("Numero total de créditos", total_creditos)