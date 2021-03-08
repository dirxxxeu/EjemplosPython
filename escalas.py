#ESCALAS
notas=['do','do#','re','re#','mi','fa','fa#','sol','sol#','la','la#','si']
seleccion=""
cont=0



cuenta=4
for x in notas[cuenta]:
    if x==11:
        x=0
        print(x)




#carga el menú y solicita una opción
def menu():
    print(""" - Menu -
Seleccione una opción
1: Escala pentatonica mayor
2: Escala pentatonica menor
3: Tonica, subdominante y dominante
0: Salir
""")

def lista_notas():
    num=0
    for i in notas:
        num+=1
        print(num,i)


while seleccion!="0":
    menu()
    seleccion=input("Eliga una opción: ")
    if seleccion=="3":
        lista_notas()
        cont=int(input("Digite una nota: "))
        print(notas[cont-1],"",notas[cont+4],"",notas[cont+6])



print("Gracias por usar el programa")
        




print("Gracias por usar el programa")

