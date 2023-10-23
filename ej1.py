#ACTIVIDAD 1
divisas = { "Euro" : "€", "Dollar" : "$", "Yen" : "Y"}
divisa = input("Introduce una divisa:")
if divisa in divisas:
    simbolo = divisas[divisa]
    print("El simbolo de su divisa es", simbolo)
else:
    print("Divisa inexistente")