"""Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
estudiante de manera individual, escriba un código en Python que permita crear un correo
electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
“@est.uca.edu.ni”"""

resp = "Si"
while(resp.upper() != "NO"):
    print("_"*60)
    print("\t--PROGRAMA PARA CREAR CORREOS ELECTRÓNICOS--\n")
    print("_"*60)
    fname = input("Ingrese su primer nombre: ")
    sname = input("Ingrese su apellido: ")
    correo = fname + "." + sname + "@est.uca.edu.ni"
    print("."*50)
    print("Su correo es: ", correo)
    print("."*50)
    resp=(input("Desea crear otro correo? SI - NO: "))
