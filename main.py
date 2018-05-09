import mesa
import random
import ficha
import equipo
import jugador
def crear_fichas():
    caja_de_ficha=[]
    for num1 in range (0,7):
        for num2 in range (0,7):
            if ficha.Ficha(num2,num1).value not in caja_de_ficha:
                caja_de_ficha.append(ficha.Ficha(num1,num2).value)
    return caja_de_ficha

def repartir_fichas():
    coleccion = crear_fichas()
    random.shuffle(coleccion)    
    mano1=coleccion[0:7]
    mano2=coleccion[7:14]
    mano3=coleccion[14:21]
    mano4=coleccion[21:28]
    return mano1,mano2,mano3,mano4
mano1,mano2,mano3,mano4=repartir_fichas()
player1=jugador.Jugador("Jose","Norte",mano1)
player2=jugador.Jugador("Laura","Este",mano2)
player3=jugador.Jugador("Fernando","Sur",mano3)
player4=jugador.Jugador("Katherine","Oeste",mano4)

def repartir_equipos(player1,player2,player3,player4):
    jugadores=[player1,player2,player3,player4]
    for element in jugadores:
        if element.posicion == "Norte":
            for each in jugadores:
                if each.posicion == "Sur":
                    equipo1 = equipo.Equipo(element,each)
                    jugadores.remove(element)
                    jugadores.remove(each)
        if element.posicion == "Sur":
            for each in jugadores:
                if each.posicion == "Norte":
                    equipo1 = equipo.Equipo(element,each)
                    jugadores.remove(element)
                    jugadores.remove(each)                    
    equipo2=equipo.Equipo(jugadores[0],jugadores[1])
    return equipo1,equipo2
equipo1,equipo2= repartir_equipos(player1,player2,player3,player4)
print(equipo1.nombres)
#equipo1 = equipo.Equipo(player1,player2)
#equipo2 = equipo.Equipo(player3,player4)


    
