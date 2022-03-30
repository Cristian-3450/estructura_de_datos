pila=[]
pila.append('LUNES')
pila.append('MARTES')
pila.append('MIERCOLES')
pila.append('JUEVES')
pila.append('VIERNES')
pila.append('SABADO')
pila.append('DOMINGO')
print(pila)
a=len(pila)
while a>1:
    x=pila.pop()
    print(pila)
    a=a-1
    