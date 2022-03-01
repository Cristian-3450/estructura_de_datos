class eliminar_duplicados:
    def eliminador(self):
        a= [10,55,14,99,1,52,21,13,1,45,22,14]
        print("Lista")
        print(a)
        for i in a:
            #b=0
            for b in a:
                if b<len(a)-1:
                    if a[i]==a[b]:
                        a[i]=0
#             while b<len(a):
#                 if b<len(a) and a[i]==a[b]:
#                     a[i]=0
#                 b=b+1
        print("Lista sin duplicados")
        print(a)
eliminar=eliminar_duplicados()
eliminar.eliminador()