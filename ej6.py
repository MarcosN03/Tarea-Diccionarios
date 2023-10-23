#Ejercicio 6
dic = {}
datos = ["edad", "sexo", "telefono"]
valores = [input("Introduzca su edad:"), input("Introduzca su sexo:"), input("Introduzca su telefono:")]
for x in datos:
    dic[x] = valores[datos.index(x)]
    print(dic)
    



