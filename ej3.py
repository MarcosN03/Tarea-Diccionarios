#ACTIVIDAD 3
frutas = {"platano" : 1.35, "manzana" : 0.80, "pera" : 0.85, "naranja" : 0.70}
fruta = input("Introduzca una fruta:")
kilos = int(input("Introduzca el nº de kilos;"))
if fruta in frutas:
    frutaselec = frutas[fruta]
    precio = frutaselec*kilos
    print("El precio será:", precio,"€")
else:
    print("No existe esa fruta")