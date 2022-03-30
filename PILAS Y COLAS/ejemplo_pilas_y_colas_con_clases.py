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
s=stack() #creando un objeto de la clase stack
print(s.estaVacio())  #muestra TRUE o FALSE
s.push(100)  #adiciona un valor
s.push(200)  #adiciona un valor
s.pop() #saca un valor (200)
print(s.size()) #1

    