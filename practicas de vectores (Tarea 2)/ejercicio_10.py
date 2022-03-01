class intercalar_vector:
    def intercalador(self):
        a=[1,3,5,7,9,11,13,15,17,19,21]
        b=[2,4,6,8,10,12,14,16,18,20]
        c=[]
        print("Lista 1:")
        print(a)
        print("Lista 2:")
        print(b)
        d=0
        e=0
        f=0
        while d<len(b)+len(a):
            if d%2!=0 and e<len(a):
                c.append(b[e])
                e=e+1
            elif d%2==0 and f<len(b):
                c.append(a[f])
                f=f+1
            d=d+1
        c.append(a[-1])
        print("Nueva lista intercalada:")
        print(c)
intercalar=intercalar_vector()
intercalar.intercalador()