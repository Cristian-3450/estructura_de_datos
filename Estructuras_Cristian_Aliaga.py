#Cristian Aliaga
def perfect(a):
    s=0
    j=a-1
    for i in range(1,j,1):
        if(a%i==0):
            s=s+i
    return s
            
class PIL:
    def __init__(self):
        self.items=[]
    def agregar(self,x):
        self.items.append(x)
    def es_vacia(self):
        return self.items==[]
    def cantidad(self):
        return len(self.items)
    def prnt(self):
        print(self.items)
pila=PIL()
s=0
op=4
while(op!=0 and op!=0):
    print("----------------------")
    print("\t\tmenu\t\t")
    print("1) Añadir elementos")
    print("2) Cargar lista")
    print("3) Mostrar lista")
    print("0) Salir")
    print("NOTA: el menu solo acepta numeros")
    op=int(input("Ingrese una opcion valida: "))
    if(op==1):
        a=int(input("ingrese la cantidad de elementos que desea agregar: "))
        for j in range(a):
            ag=int(input("Ingrese un valor: "))
            pila.agregar(ag)
    elif(op==2):
        for h in range(1,10,1):
            s=perfect(h)
            if(s!=0):
                pila.agregar(s)
    elif(op==3):
        cant=pila.cantidad()
        print("La cantidad de elementos de la lista es: ",cant)
        pila.prnt()
            
        