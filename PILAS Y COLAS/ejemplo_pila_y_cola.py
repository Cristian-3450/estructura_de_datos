pila=[]
cola=[]
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
    print()
    x=pila.pop()
    print('pila:')
    print(pila)
    print()
    cola.append(x)
    print('cola:')
    print(cola)
    a=a-1