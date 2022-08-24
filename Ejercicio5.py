#Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
#enteros.

numIni= int(input("Escribe el numero inicial: "))
numFin= int(input("Escribe el numero final: "))

for i in range(numIni,numFin):
    if i%2==0 :
        print(i)
