#Mostrar el total a pagar por la compra de n cantidad de productos a un precio
#desconocido.
productos = []
resp = "Si"
producto = 0
num = 1
while(resp.upper() != "NO"):
    try:
        print("Escribe el precio del producto", num, ": " )
        producto = int(input())
        resp=(input("Desea agregar otro producto? SI - NO: "))
        productos.append(producto)
        num +=1
    except Exception as ex: 
        print("Error. ", str(ex), "Intente de nuevo")

suma= sum(productos)
print("El total es de: ", suma)