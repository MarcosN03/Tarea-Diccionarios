#ACTIVIDAD 4
meses = {"01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio", "07": "Julio", "08": "Agosto", "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"}
fecha = str(input("Introduce una fecha en formato dd/mm/aaaa:"))
dia = fecha[0:2]
mes = fecha[3:5]
año = fecha[6:10]
if mes in meses:
    mes_selec = meses[mes]
    print(dia,"de",mes_selec,"del",año)
else:
    print("No existe esa fecha")
