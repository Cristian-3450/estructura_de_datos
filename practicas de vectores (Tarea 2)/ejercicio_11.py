class definir_max_min_cero:
    def definidor(self):
        a=[80,-10,72,0,45,0,-5]
        p,n,cero = 0,0,0
        for i in range(0,len(a),1):
            if a[i]>0:
                p=p+1
            elif a[i]<0:
                n=n+1
            elif a[i]==0:
                cero=cero+1
        print("Positivos:",p,"Negativos:",n,"Ceros:",cero)
Definir=definir_max_min_cero()
Definir.definidor()
        