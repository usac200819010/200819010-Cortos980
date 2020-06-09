print('''
      
     
    si el número es par, se lo divide por dos;
    si es impar, se le multiplica tres y se le suma uno;
    la sucesión termina al llegar a uno.
 
      
      ''')


#carnet 200819010

inicio = 10

modulo = 0
valor = True
sig = 0
lista = []
while valor :
        #del lista[:]
        for i in range(2, inicio+1):
            modulo = i%2 #si el modulo es 0 es par si es 1 es impar
            
            if inicio == 10:
                valor = False        

            if modulo == 1:
                sig = int(3*i+1)
                #print(i,sig, "impar")
                inicio = sig
                lista.append(sig)
            else:
                sig = int(i/2)
                #print(sig)
                inicio = sig
                #print(i,sig, "par")
                lista.append(sig)   
            inicio = lista[-1]     
            print(i, lista[-1], inicio,lista)
            
        archivo = open('collatz.txt', 'w')
        
                


        
#print(lista, ": ", len(lista) )
#print("la secuencia Collatz está dada por: ",lista )