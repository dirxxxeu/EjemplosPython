def verificar(texto):
    
    comparacion=[]
    toriginal=texto.lstrip()
    toriginal=texto.lower()
    
    for a in range(len(toriginal)):
        
        if toriginal[a]==" ":
            continue
        comparacion.append(toriginal[a])
    comparar(texto,comparacion)
    
def comparar(texto,comparacion):
    
    treves=[]
    b=len(comparacion)-1
    a=0

#carga la frase y la ingresa en una lista al reves
    while a<=b:
                     
        treves.append(comparacion[b])   
        b-=1

    
    print(treves)
    print(comparacion)
#hace la comparación de frases almacenadas en las listas treves y comparacion
    if treves==comparacion:
        print("Si es un palindromo")
    else:
        print("No es un palindromo")




#ingrese la frase para saber si es palindromo
texto=input("Escriba el texto que de sea saber si es palindromo ")

#pasa a la funcion verificar
verificar(texto)
