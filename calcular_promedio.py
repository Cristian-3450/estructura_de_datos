# a=[]
# b=int(input("Ingrese la cantidad de notas que desea promediar: "))
# suma=0
# for i in range(0,b,1):
#     a.append(int(input("Ingrese nota: ")))
#     suma=suma+i
# p=suma/len(a)
# print("El promedio de las notas es: ",p)
notas=input("Ingrese las notas separadas por comas: ")
notas=notas.split(',')
tam=len(notas)
suma=0
sumsq=0
# for i in range(tam):
#     notas[i]=int(notas[i])
for x in notas:
    suma=suma+int(x)
    sumsq+=int(x)**2
p=int(suma/tam)
stdev=(sumsq/tam-p**2)**(1/2)

print("El promedio es: ",p)
print("La desviacion tipica es: ",stdev)