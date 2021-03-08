

#segun los números digitados, se escoge en las
#condicionales y los muestra en pantalla
def matriz(n):
    


    if n=="1":
        lista=[" ","#"," "," ","#"," "," ","#"," "," ","#"," "," ","#"," "]
        for i in range(len(lista)):
            if i==2 or i==5 or i==8 or i==11 or i==14:
                print(lista[i],"\n")
            else:
                print(lista[i],end="")
    if n=="2":
        lista=["#","#","#"," "," ","#","#","#","#","#"," "," ","#","#","#"]
        for i in range(len(lista)):
            if i==2 or i==5 or i==8 or i==11 or i==14:
                print(lista[i],"\n")
            else:
                print(lista[i],end="")
     
    if n=="3":
       lista=["#","#","#"," "," ","#","#","#","#"," "," ","#","#","#","#"]
       for i in range(len(lista)):
           if i==2 or i==5 or i==8 or i==11 or i==14:
               print(lista[i],"\n")
           else:
               print(lista[i],end="")

    if n=="4":
       lista=["#"," ","#","#"," ","#","#","#","#"," "," ","#"," "," ","#"]
       for i in range(len(lista)):
           if i==2 or i==5 or i==8 or i==11 or i==14:
               print(lista[i],"\n")
           else:
               print(lista[i],end="")
    if n=="5":
       lista=["#","#","#","#","-","-","#","#","#","-","-","#","#","#","#"]
       for i in range(len(lista)):
           if i==2 or i==5 or i==8 or i==11 or i==14:
               print(lista[i],"\n")
           else:
               print(lista[i],end="")

    if n=="6":
       lista=["#","#","#","#","-","-","#","#","#","#","-","#","#","#","#"]
       for i in range(len(lista)):
           if i==2 or i==5 or i==8 or i==11 or i==14:
               print(lista[i],"\n")
           else:
               print(lista[i],end="")
    if n=="7":
       lista=["#","#","#"," "," ","#"," "," ","#"," "," ","#"," "," ","#"]
       for i in range(len(lista)):
           if i==2 or i==5 or i==8 or i==11 or i==14:
               print(lista[i],"\n")
           else:
               print(lista[i],end="")
    if n=="8":
       lista=["#","#","#","#","-","#","#","#","#","#","-","#","#","#","#"]
       for i in range(len(lista)):
           if i==2 or i==5 or i==8 or i==11 or i==14:
               print(lista[i],"\n")
           else:
               print(lista[i],end="")
    if n=="9":
       lista=["#","#","#","#"," ","#","#","#","#"," "," ","#"," "," ","#"]
       for i in range(len(lista)):
           if i==2 or i==5 or i==8 or i==11 or i==14:
               print(lista[i],"\n")
           else:
               print(lista[i],end="")
    if n=="0":
       lista=["#","#","#","#"," ","#","#"," ","#","#"," ","#","#","#","#"]
       for i in range(len(lista)):
           if i==2 or i==5 or i==8 or i==11 or i==14:
               print(lista[i],"\n")
           else:
               print(lista[i],end="")               
               
def funcion(x):    

    list(x)
    
    for i in range(len(x)):
        
        numeros=x[i]
        matriz(numeros)
    
    
#inicia el programa y solicita ingresar la opción y luego lo muestra
x=funcion(input("Digite opcion: "))
