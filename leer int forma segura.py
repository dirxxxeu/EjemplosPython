#funcion para leer el número ingresado. 
def readint(prompt, min, max):
   
   while prompt:      
           
      try:
         numero=int(input("Digite un numero del -10 al 10: "))
         parametros=numero >= -10 and numero<= 10
         if parametros:
            return numero
         else:
            print("Ingrese un numero valido")
      except ValueError:
         print("Debe digitar un numero, no una letra" )
         

#El programa inicia leyendo esta línea
v = readint("Enter a number from -10 to 10: ", -10, 10)



print("El numero es:", v)
