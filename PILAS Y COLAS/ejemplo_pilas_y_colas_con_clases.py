class stack:
    def __init__(self):
        self.items=[]
    def estaVacio(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        return slef.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s=stack() # creando un objeto de la clase stack
# print(s.estaVacio())  # muestra TRUE o FALSE
# s.push(100)  # adiciona un valor
# s.push(200)  # adiciona un valor
# s.pop() # saca un valor (200)
# print(s.size()) # 1
#print(s.estaVacio())  # muestra TRUE o FALSE
n=int(input("ingrese la cantidad de elementos que desea ingresar: "))
for i in range(0,n,1):
    e=input("ingrese el elemento: ")
    s.push(e)
print(s.size())
p=input("desea sacar un elemento(s/n):")
while p=='s' or p=='S':
    if s.estaVacio() != True:
        s.pop()
        print("Tamaño: ",s.size())
        p=input("desea sacar otro elemento(s/n):")
    else:
        print("La pila esta vacia no se puede sacar mas elementos")
        p='n'
        
    
    