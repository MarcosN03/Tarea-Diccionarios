#ACTIVIDAD 2
nombre = input("Introduce un nombre:")
edad = input("Introduce una edad:")
direccion = input("Introudce una direccion:")
telefono = input("Introduce un telefono:")
datos = { "nombre" : nombre, "edad" : edad, "direccion" : direccion, "telefono" : telefono}
print(datos.get("nombre"), "tiene",datos.get("edad"), ",vive en",datos.get("direccion"), "y su numero de telefono es",datos.get("telefono"))
