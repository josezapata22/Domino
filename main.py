import operator
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
player2=jugador.Jugador("Laura","Sur",mano2)
player3=jugador.Jugador("Fernando","Este",mano3)
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
def repartir_turnos(player1,player2,player3,player4):
    
    jugadores=[player1,player2,player3,player4]
    for element in jugadores:
        if ficha.Ficha(6,6).value in element.mano:
            element.turno = 1
            if element.posicion == "Norte":
                for nino in jugadores:
                    if nino.posicion == "Oeste":
                        nino.turno = 2
                    if nino.posicion == "Sur":
                        nino.turno = 3
                    if nino.posicion == "Este":
                        nino.turno = 4    
            if element.posicion == "Este":
                for nino in jugadores:
                    if nino.posicion == "Oeste":
                        nino.turno = 3
                    if nino.posicion == "Sur":
                        nino.turno = 4
                    if nino.posicion == "Norte":
                        nino.turno = 2                   
            if element.posicion == "Sur":
                for nino in jugadores:
                    if nino.posicion == "Oeste":
                        nino.turno = 4
                    if nino.posicion == "Norte":
                        nino.turno = 3
                    if nino.posicion == "Este":
                        nino.turno = 2
            if element.posicion == "Oeste":
                for nino in jugadores:
                    if nino.posicion == "Este":
                        nino.turno = 3
                    if nino.posicion == "Sur":
                        nino.turno = 2
                    if nino.posicion == "Norte":
                        nino.turno = 4    
                        

def test():
    repartir_turnos(player1,player2,player3,player4)
    
    print(player1.mano)
    print(str(player1.turno)+ " "+ player1.posicion)
    
    print (player2.mano)
    print(str(player2.turno)+ " "+ player2.posicion)
    
    print(player3.mano)
    print(str(player3.turno)+ " "+ player3.posicion)
    
    print(player4.mano)
    print(str(player4.turno)+ " "+ player4.posicion)    

lista_jugadores=[player1,player2,player3,player4]
test()
mesita=mesa.Mesa(equipo1,equipo2)
lista_jugadores.sort(key=operator.attrgetter('turno'))#funcion del modulo operator, que busca ese atributo en el objeto iterado
for element in lista_jugadores:
    print(element.nombre)
    
jugada=0
while len(mesita.juego)<28:
    
    if jugada > 3:
        jugada=0
    print(mesita.juego)
    if len(mesita.juego)==0:
        print("{} Comienza con doble 6!\n".format(lista_jugadores[jugada].nombre))
        print(lista_jugadores[jugada].mano)
        elegida=input()
        indice_ficha= int(elegida) - 1
        ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
        lista_jugadores[jugada].mano.remove(ficha_elegida)
        mesita.juego.append(ficha_elegida)
        jugada+=1
        print("\n"*10)
        continue
    else:
        for cada_una in lista_jugadores[jugada].mano:
            if  mesita.juego[-1][-1] == cada_una[0]:
                print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                print(lista_jugadores[jugada].mano)
                elegida=input()
                indice_ficha= int(elegida) - 1
                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                lista_jugadores[jugada].mano.remove(ficha_elegida) 
                mesita.juego.append(ficha_elegida)
                jugada+=1
                break
            if mesita.juego[-1][-1] == cada_una[1]:
                print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                print(lista_jugadores[jugada].mano)
                elegida=input()
                indice_ficha= int(elegida) - 1
                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                lista_jugadores[jugada].mano.remove(ficha_elegida)
                mesita.juego.append(ficha_elegida[::-1])
                jugada+=1
                break                
            if  mesita.juego[0][0] == cada_una[1]:
                print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                print(lista_jugadores[jugada].mano)
                elegida=input()
                indice_ficha= int(elegida) - 1
                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                lista_jugadores[jugada].mano.remove(ficha_elegida) 
                mesita.juego.insert(0,ficha_elegida) 
                jugada+=1
                break
            if mesita.juego[0][0] == cada_una[0]:
                print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                print(lista_jugadores[jugada].mano)
                elegida=input()
                indice_ficha= int(elegida) - 1
                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                lista_jugadores[jugada].mano.remove(ficha_elegida) 
                mesita.juego.insert(0,ficha_elegida[::-1]) 
                jugada+=1
                break                
            
    
    print("\n"*10)
    
    







    
