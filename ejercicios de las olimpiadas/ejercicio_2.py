n=int(input("ingrese un numero entero positivo: "))
# suma=n*(n+1)/2
suma=int(0)
for i in range(1,n+1,1):
    suma=suma+i
print("La suma de los primeros numeros de 1 hasta "+str(n)+" es " +str(suma))
