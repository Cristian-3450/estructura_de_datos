def factorial(numero):
    if numero>1:
        numero=numero * factorial(numero-1)
    elif numero==1:
        return numero
    else:
        if numero==0:
            return numero+1
        print("los numeros negativos no tienen factorial")
    return numero
    print("Fin de la funcion")
fac=int (input("ingrese un numero: "))
if factorial(fac)>0:
    print("El factorial de ",fac," es ",factorial(fac))
else:
    print(factorial(fac))
    
