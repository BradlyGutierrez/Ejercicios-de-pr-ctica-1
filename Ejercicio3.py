#Aplicar el IVA al precio de un producto.
productos = []
resp = "Si"
producto = 0
num = 1
while(resp.upper() != "NO"):
    try:
        print("Escribe el precio del producto", num, ": " )
        producto = int(input())
        print("EL precio del producto con IVA es de: ", producto +(producto*0.15))
        resp=(input("Desea agregar otro producto? SI - NO: "))
        productos.append(producto)
        num +=1
    except Exception as ex: 
        print("Error. ", str(ex), "Intente de nuevo")

suma= sum(productos)
print("El total es de: ", suma)
print("El precio con IVA es de: ", suma + suma*0.15)