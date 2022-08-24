"""Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro."""
print("_"*50)
numDeCuenta = int(input("\t Ingrese su número de cuenta \n"))
print("_"*50)
saldoActual = 600
print("Su saldo actual es de: ", saldoActual)
retiro = float(input(" \t Escriba la cantidad a retirar \n"))
print("_"*50)

if saldoActual < retiro: 
    print("_"*50)
    print("Lo sentimos, no tiene los suficientes fondos")
elif saldoActual == retiro:
    print("_"*50) 
    print("Su cuenta quedará en cero")
else: 
    print("_"*50)
    print("Saldo despues del retiro: ", saldoActual- retiro)