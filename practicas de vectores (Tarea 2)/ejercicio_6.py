class Promedio_cada_tres:
    def promedio(self):
        a=[4,5,9,7,8,30]
        b=0
        sum=0
        for i in a:
            sum=sum+i
            b+=1
            if b==3:
                print("El promedio es: "+str(sum/3))
                b=0
                sum=0
           
promedio_tres=Promedio_cada_tres()
promedio_tres.promedio()
            
            
            