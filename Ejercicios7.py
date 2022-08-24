#Leer x cantidad de edades y mostrar el promedio de dichas edades.
from statistics import mean, median, mode
import statistics
edades = []
resp = "Si"
edad = 0
num = 1
while(resp.upper() != "NO"):
    try:
        print("Escribe la edad del sujeto ", num, ": " )
        edad = int(input())
        resp=(input("Desea agregar otra edad? SI - NO: "))
        edades.append(edad)
        num += 1
    except Exception as ex: 
        print("Error. ", str(ex), "Intente de nuevo")
promedio = statistics.mean(edades)
print("El promedio de edades es de: ", promedio)
