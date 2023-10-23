#EJERCICIO7
dic = {}
seguir = True
total = 0
while seguir:
    articulo = input("Introduzca su articulo:")
    presio = int(input("Introduzca su precio:"))
    dic[articulo] = presio
    total += presio
    seguir = input("¿Quieres seguir añadiendo articulos? (Si/No)") == "Si"
for x in dic:
    print(x, dic[x])      
print("Total:",total)    


