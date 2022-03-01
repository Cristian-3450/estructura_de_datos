class Convertir:
    def convertidor(self):
        dic={0:"cero",1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve",10:"diez",11:"once",12:"doce",13:"trece",14:"catorce",15:"quince",16:"dieciseis",17:"diecisiete",18:"dieciocho",19:"diecinueve",20:"veinte"}
        print("Convertir un numero (por ejemplo 12) a su equivalente en literal (doce),solo numeros del 0 al 20")
        numero=int(input("Ingrese un numero: "))
        if numero<20:
            c=0
            while c<20:
                if numero==c:
                    print("El numero:"+str(numero)+" en literal es: "+dic[c])
                c+=1
        else:
            print("El numero digitado no esta dentro de los parametros.")
convertir=Convertir()
convertir.convertidor()