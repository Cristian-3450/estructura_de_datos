def contar(x):
    conta=[]
    for i in x:
        r=x.count(i)
        if(r>1):
            conta.append(i)
    return conta
def rep1(x,y):
    rep=[]
    for i in x:
        for j in y:
            if(i==j):
                rep.append(i)
    return rep
def rep2(x,y):
    repe=[]
    for i in y:
        for j in x:
            if(i!=j):
                repe.append(j)
                repe.append(i)
    return repe
def remov(x,y):
        for i in x:
            for j in y:
                if(j==i):
                    y.remove(j)
        return y
Primario=[]

Secundario=[]

print("nombres de primaria (para dejar de ingresar nombres ingrese la letra x)")
nomp=str(input("ingrese el nombre de pila del alumno de primaria: "))

while (nomp!='x'):
    Primario.append(nomp)
    nomp=str(input("ingrese el nombre de pila del alumno de primaria: "))

    

    
print("nombres de secundaria (para dejar de ingresar nombres ingrese la letra x)")
noms=str(input("ingrese el nombre de pila del alumno de secundaria: "))

while (noms!='x'):
    Secundario.append(noms)
    noms=str(input("ingrese el nombre de pila del alumno de secundaria: "))


    
repP=contar(Primario)
repS=contar(Secundario)
Primario=list(set(Primario))
Secundario=list(set(Secundario))
print("Nivel Primario: ", Primario)
print("Nivel Secundario: ", Secundario)
repetidos=rep1(Primario,Secundario)
norepetidos=rep2(Primario,Secundario)
repetidos=list(set(repetidos))
norepetidos=list(set(norepetidos))
norepetidos2=remov(repetidos,norepetidos)
print("Nombres repetidos: ", repetidos)
print("Nombres no repetidos: ", norepetidos2)


