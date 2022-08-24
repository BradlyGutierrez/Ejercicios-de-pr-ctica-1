#Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.
precios = []
resp = "Si"
precio = 0
num = 1
while(resp.upper() != "NO"):
    try:
        print("Escribe el precio del producto ", num, ": " )
        precio = int(input())
        resp=(input("Desea agregar otro precio? SI - NO: "))
        precios.append(precio)
        num += 1
    except Exception as ex: 
        print("Error. ", str(ex), "Intente de nuevo")

print("El numero mayor es: ", max(precios))
