import mesa
import ficha
import equipo
import jugador
def crear_fichas():
    caja_de_ficha=[]
    for num1 in range (1,7):
        for num2 in range (1,7):
            if ficha.Ficha(num2,num1).value not in caja_de_ficha:
                caja_de_ficha.append(ficha.Ficha(num1,num2).value)

    return caja_de_ficha
coleccion = crear_fichas()
print (coleccion)
#def main():
    
    #mesita= mesa.Mesa()
    #coleccion= mesita.crear_fichas()
    #print(coleccion)

#jugador1= jugador.Jugador("jose","norte",)
#main()