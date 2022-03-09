a=[]
b=int(input("Ingrese el rango del vector: "))
for i in range (0,b,1):
    a.append(int(input("Ingrese un numero: ")))
    
a.sort()
print("Los numeros ordenados de menor a mayor son:"+str(a))
a.sort(reverse=True)
print("Los numeros ordenados de mayor a menor son:"+str(a))