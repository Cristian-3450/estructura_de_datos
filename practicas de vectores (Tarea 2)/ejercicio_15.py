class ordenar_ascendente:
    def orden_ascendente(self):
        a=[50,36,88,51,55,21,77,60,100,46]
        b=["juan carlos","andres","mauricio","julio","marco","andrea","maria jose","marco antonio","miguel","angel"]
        print("lista de notas")
        c=0
        while c<len(a):
            print(b[c],"------",a[c])
            c+=1
        a.sort(reverse=True)
        b.sort(reverse=True)
        c=0
        print()
        print()
        print("lista de las tres mejores notas")
        while c<3:
            print(b[c],"------",a[c])
            c+=1
ordenar=ordenar_ascendente()
ordenar.orden_ascendente()
