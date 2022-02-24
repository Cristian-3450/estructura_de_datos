peso=input("ingrese su peso en Kg.: ")
altura=input("ingrese su altura en metros: ")
imc=round(float(peso)/float(altura)**2,2)
print("Su IMC es: "+str(imc))