class Concatenar:
    def concatenador(self):
        a=[1,3,5,7,9,11]
        b=[2,4,6,8,10,12,14,16,18,20]
        print("lista 1")
        print(a)
        print("lista 2")
        print(b)
        contador=len(a)
        for i in b:
            a.append(i)
            contador=contador+1
        print("Lista concatenada(lista 1 + lista 2)")
        print(a)
        print("total de objetos de la lista concatenada")
        print(contador)
concatenar=Concatenar()
concatenar.concatenador()