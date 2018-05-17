import operator
import mesa
import random
import ficha
import equipo
import jugador
def contar_fichas_totales(ficha_en_mesa):
    if ficha_en_mesa[0] == 0 or ficha_en_mesa[1] == 0:
        mesita.f0+=1
    if ficha_en_mesa[0] == 1 or ficha_en_mesa[1] == 1:
        mesita.f1+=1        
    if ficha_en_mesa[0] == 2 or ficha_en_mesa[1] == 2:
        mesita.f2+=1
    if ficha_en_mesa[0] == 3 or ficha_en_mesa[1] == 3:
        mesita.f3+=1  
    if ficha_en_mesa[0] == 4 or ficha_en_mesa[1] == 4:
        mesita.f4+=1
    if ficha_en_mesa[0] == 5 or ficha_en_mesa[1] == 5:
        mesita.f5+=1  
    if ficha_en_mesa[0] == 6 or ficha_en_mesa[1] == 6:
        mesita.f6+=1                
def contar_fichas_tranque(trancador,siguiente):
    total_trancador = 0
    total_siguiente = 0
    for each in trancador.mano:
        total_trancador += each.value[0] + each.value[1]
    for each in siguiente.mano:
        total_siguiente += each.value[0] + each.value[1]
    if total_trancador <= total_siguiente:
        return trancador
    else:
        return siguiente
def sumar_puntos(lista_jugadores):
    suma=0
    for element in range(0,len(lista_jugadores)):
        for pieza in lista_jugadores[element].mano:
            suma+= pieza.value[0]+pieza.value[1]
    return suma

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
def validar_jugada(mesa_izquierda,mesa_derecha,mano):
    index=0
    while index < len(mano):
        
        if mesa_izquierda in mano[index] or mesa_derecha in mano[index]:
            return True
        if mesa_izquierda not in mano[index] and mesa_derecha not in mano[index] and index == len(mano)-1:
            return False
        index+=1
def validar_pieza(extremo_izq,extremo_der,pieza):
    if extremo_izq in pieza or extremo_der in pieza:
        return True
    return False
def validar_doble_6(pieza):
    if pieza[0] == 6 and pieza[1] == 6 :
        return True
    return False
ganador=False
while ganador==False:
    
    if jugada > 3:
        jugada=0
     
    print(mesita.juego)
    if len(mesita.juego)==0:
        print("{} Comienza con doble 6!\n".format(lista_jugadores[jugada].nombre))
        print(lista_jugadores[jugada].mano)
        elegida=input()
        indice_ficha= int(elegida) - 1
        ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
        if not validar_doble_6(ficha_elegida):
            while validar_doble_6(ficha_elegida) == False:
                print("Esta ficha no es el doble 6, por favor seleccione la ficha correcta!\n")
                print(mesita.juego)
                print("{}:".format(lista_jugadores[jugada].nombre))
                print(lista_jugadores[jugada].mano)
                elegida=input()
                indice_ficha= int(elegida) - 1
                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                
        contar_fichas_totales(ficha_elegida)
        lista_jugadores[jugada].mano.remove(ficha_elegida)
        mesita.juego.append(ficha_elegida)
        jugada+=1
        print("\n"*10)
        continue
    if (mesita.juego[0][0] == mesita.juego[-1][-1])and mesita.juego[0][0] == 0 and mesita.f0== 6:
        input("{} Ha trancado el juego!".format(lista_jugadores[jugada].nombre))
        ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada])
        input ("El ganador del juego es: {} !!!".format(ganador.nombre))
        break
    if (mesita.juego[0][0] == mesita.juego[-1][-1])and mesita.juego[0][0] == 1 and mesita.f1 == 6:
        input("{} Ha trancado el juego!".format(lista_jugadores[jugada].nombre))
        ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada])
        input ("El ganador del juego es: {} !!!".format(ganador.nombre))
        break     
    if (mesita.juego[0][0] == mesita.juego[-1][-1])and mesita.juego[0][0] == 2 and mesita.f2 == 6:
        input("{} Ha trancado el juego!".format(lista_jugadores[jugada].nombre))
        ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada])
        input ("El ganador del juego es: {} !!!".format(ganador.nombre))
        break     
    if (mesita.juego[0][0] == mesita.juego[-1][-1])and mesita.juego[0][0] == 3 and mesita.f3 == 6:
        input("{} Ha trancado el juego!".format(lista_jugadores[jugada].nombre))
        ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada])
        input ("El ganador del juego es: {} !!!".format(ganador.nombre))
        break     
    if (mesita.juego[0][0] == mesita.juego[-1][-1])and mesita.juego[0][0] == 4 and mesita.f4 == 6:
        input("{} Ha trancado el juego!".format(lista_jugadores[jugada].nombre))
        ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada])
        input ("El ganador del juego es: {} !!!".format(ganador.nombre))
        break     
    if (mesita.juego[0][0] == mesita.juego[-1][-1])and mesita.juego[0][0] == 5 and mesita.f5 == 6:
        input("{} Ha trancado el juego!".format(lista_jugadores[jugada].nombre))
        ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada])
        input ("El ganador del juego es: {} !!!".format(ganador.nombre))
        break     
    if (mesita.juego[0][0] == mesita.juego[-1][-1]) and mesita.juego[0][0] == 6 and mesita.f6 == 6:
        input("{} Ha trancado el juego!".format(lista_jugadores[jugada].nombre))
        ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada])
        input ("El ganador del juego es: {} !!!".format(ganador.nombre))
        break         
    
    
    else:
        
        for cada_una in lista_jugadores[jugada].mano:
            if validar_jugada(mesita.juego[0][0],mesita.juego[-1][-1],lista_jugadores[jugada].mano):
                    
                if  mesita.juego[-1][-1] == cada_una[0]:
                    print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                    print(lista_jugadores[jugada].mano)
                    elegida=input()
                    indice_ficha= int(elegida) - 1
                    ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                    if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                        while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) == False:
                            print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                            print(mesita.juego)
                            print("{}:".format(lista_jugadores[jugada].nombre))
                            print(lista_jugadores[jugada].mano)
                            elegida=input()
                            indice_ficha= int(elegida) - 1
                            ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                    
                    contar_fichas_totales(ficha_elegida)
                    lista_jugadores[jugada].mano.remove(ficha_elegida) 
                    mesita.juego.append(ficha_elegida)                                                        
                    
                    if len(lista_jugadores[jugada].mano) == 0:
                        print("{} Ha ganado el juego!,ya termino todas sus fichas!\n".format(lista_jugadores[jugada].nombre))
                        ganador=True
                    jugada+=1
                    break
                if mesita.juego[-1][-1] == cada_una[1]:
                    print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                    print(lista_jugadores[jugada].mano)
                    elegida=input()
                    indice_ficha= int(elegida) - 1
                    ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                    if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                        while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) ==  False:
                            print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                            print(mesita.juego)
                            print("{}:".format(lista_jugadores[jugada].nombre))
                            print(lista_jugadores[jugada].mano)                            
                            elegida=input()
                            indice_ficha= int(elegida) - 1
                            ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                      
                    contar_fichas_totales(ficha_elegida)
                    lista_jugadores[jugada].mano.remove(ficha_elegida)
                    mesita.juego.append(ficha_elegida[::-1])
                    if len(lista_jugadores[jugada].mano) == 0:
                        print("{} Ha ganado el juego!,ya termino todas sus fichas!\n".format(lista_jugadores[jugada].nombre))
                        ganador=True                    
                    jugada+=1
                    break                
                if  mesita.juego[0][0] == cada_una[1]:
                    print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                    print(lista_jugadores[jugada].mano)
                    elegida=input()
                    indice_ficha= int(elegida) - 1
                    ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                    if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                        while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) == False:
                            print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                            print(mesita.juego)
                            print("{}:".format(lista_jugadores[jugada].nombre))
                            print(lista_jugadores[jugada].mano)                            
                            elegida=input()
                            indice_ficha= int(elegida) - 1
                            ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                      
    
                    contar_fichas_totales(ficha_elegida)
                    lista_jugadores[jugada].mano.remove(ficha_elegida) 
                    mesita.juego.insert(0,ficha_elegida) 
                    if len(lista_jugadores[jugada].mano) == 0:
                        print("{} Ha ganado el juego!,ya termino todas sus fichas!\n".format(lista_jugadores[jugada].nombre))
                        ganador=True                    
                    jugada+=1
                    break
                if mesita.juego[0][0] == cada_una[0]:
                    print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                    print(lista_jugadores[jugada].mano)
                    elegida=input()
                    indice_ficha= int(elegida) - 1
                    ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                    if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                        while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) == False:
                            print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                            print(mesita.juego)
                            print("{}:".format(lista_jugadores[jugada].nombre))
                            print(lista_jugadores[jugada].mano)                            
                            elegida=input()
                            indice_ficha= int(elegida) - 1
                            ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                      
                    contar_fichas_totales(ficha_elegida)
                    lista_jugadores[jugada].mano.remove(ficha_elegida) 
                    mesita.juego.insert(0,ficha_elegida[::-1]) 
                    if len(lista_jugadores[jugada].mano) == 0:
                        print("{} Ha ganado el juego!,ya termino todas sus fichas!\n".format(lista_jugadores[jugada].nombre))
                        ganador=True                    
                    jugada+=1
                    break                
            
            else:
                print("{} no tiene fichas disponibles!\n".format(lista_jugadores[jugada].nombre))
                print(lista_jugadores[jugada].mano)
                input()
                jugada+=1
                break
    print("\n"*10)
    




    
