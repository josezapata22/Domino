import os
import operator
import mesa
import random
import ficha
import equipo
import jugador
def contar_fichas_totales(ficha_en_mesa,mesita):
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
def contar_fichas_tranque(trancador,siguiente,lista_jugadores):
    total_trancador = 0
    total_siguiente = 0
    input("{}: Fichas de {}'Trancador'\n{}: Fichas de {}'Jugador siguiente'\n ".format(trancador.mano,trancador.nombre,siguiente.mano,siguiente.nombre) )
    for each in trancador.mano:
        total_trancador += each[0] + each[1]
    for each in siguiente.mano:
        total_siguiente += each[0] + each[1]
    if total_trancador <= total_siguiente:
        trancador.puntos=sumar_puntos(lista_jugadores,capicua)
        return trancador,trancador
    else:
        siguiente.puntos=sumar_puntos(lista_jugadores,capicua)
        return siguiente
def sumar_puntos(lista_jugadores,capicua):
    suma=0
    for element in lista_jugadores:
        for fichas in element.mano:
            suma += fichas[1]+fichas[0]
              
    if capicua == True:
        suma+=25
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
                        
def test(player1,player2,player3,player4):
    repartir_turnos(player1,player2,player3,player4)
    
    print(player1.mano)
    print(str(player1.turno)+ " "+ player1.posicion)
    
    print (player2.mano)
    print(str(player2.turno)+ " "+ player2.posicion)
    
    print(player3.mano)
    print(str(player3.turno)+ " "+ player3.posicion)
    
    print(player4.mano)
    print(str(player4.turno)+ " "+ player4.posicion)    


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
def crear_jugadores():
    n=1
    posiciones=["Norte","Sur","Este","Oeste"]
    player1=jugador.Jugador(None,None,None)
    player2=jugador.Jugador(None,None,None)
    player3=jugador.Jugador(None,None,None)
    player4=jugador.Jugador(None,None,None)
    jugadores=[player1,player2,player3,player4]
    for element in jugadores:
        element.nombre= input("Digite el nombre del jugador {}\n".format(n))
        indice_pos=int(input("Estas son las posiciones dispobnibles -->{}  Seleccione cual desea.\n".format(posiciones)))-1
        element.posicion=posiciones[indice_pos]
        posiciones.pop(indice_pos)  
        n+=1
    mano1,mano2,mano3,mano4=repartir_fichas()
    player1.mano=mano1
    player2.mano=mano2
    player3.mano=mano3
    player4.mano=mano4
    variable_pa_borrar=os.system('cls')
    return player1,player2,player3,player4
def game():
    partidas=0      
    player1,player2,player3,player4=crear_jugadores()
    lista_jugadores=[player1,player2,player3,player4]    
    repartir_turnos(player1,player2,player3,player4)
    equipo1,equipo2= repartir_equipos(player1,player2,player3,player4)
    mesita=mesa.Mesa(equipo1,equipo2)
    lista_jugadores.sort(key=operator.attrgetter('turno'))#funcion del modulo operator, que busca ese atributo en el objeto iterado
    while equipo1.puntos <= 200 and equipo2.puntos <= 200:
        capicua=False
        equipo1.puntos += equipo1.player1.puntos + equipo1.player2.puntos
        equipo2.puntos += equipo2.player1.puntos + equipo2.player2.puntos
        player1.puntos = 0
        player2.puntos = 0
        player3.puntos = 0
        player4.puntos = 0        
        mesita.juego = []
        mesita.f0=0
        mesita.f1=0
        mesita.f2=0
        mesita.f3=0
        mesita.f4=0
        mesita.f5=0
        mesita.f6=0
        mano1,mano2,mano3,mano4=repartir_fichas()
        player1.mano = []
        player2.mano = []
        player3.mano = []
        player4.mano = []
        player1.mano = mano1
        player2.mano = mano2
        player3.mano = mano3
        player4.mano = mano4         
        #lista_jugadores=[player1,player2,player3,player4]
        if partidas == 0:
            repartir_turnos(player1,player2,player3,player4)
        lista_jugadores.sort(key=operator.attrgetter('turno'))
        if partidas == 0:
            jugada=0
        ganadora=False
        
        
        if (equipo1.puntos >= 200 or equipo2.puntos >= 200):
            if equipo1.puntos >= 200:
                input("El equipo ganador es el de {} !!!\n".format(equipo1.nombres))
                break
            if equipo2.puntos >= 200:
                input("El equipo ganador es el de {} !!!\n".format(equipo2.nombres))
                break
        if not  partidas == 0:#recordar ponerle el not pa que no salga en el eprimer turno
            input("Equipo de {} , {} puntos!\nEquipo de {} , {} puntos!!!\n".format(equipo1.nombres,equipo1.puntos,equipo2.nombres,equipo2.puntos))
            variable_pa_borrar=os.system('cls')
        while ganadora==False:
            
            if jugada > 3:
                jugada=0
             
            print(mesita.juego)
            if len(mesita.juego)==0 and partidas == 0:
                print("{} Comienza con doble 6!\n".format(lista_jugadores[jugada].nombre))
                print(lista_jugadores[jugada].mano)
                elegida=input()
                while  (int(elegida) -1) >= len(lista_jugadores[jugada].mano):
                    print(lista_jugadores[jugada].mano)
                    elegida=input("No existe esa ficha, porfavor tome una de sus opciones!\n")
                    
                indice_ficha= int(elegida) - 1
                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                if not validar_doble_6(ficha_elegida):
                    while validar_doble_6(ficha_elegida) == False:
                        print("Esta ficha no es el doble 6, por favor seleccione la ficha correcta!\n")
                        print(mesita.juego)
                        print("{}:".format(lista_jugadores[jugada].nombre))
                        print(lista_jugadores[jugada].mano)
                        elegida=input()
                        while  (int(elegida) -1) >= len(lista_jugadores[jugada].mano):
                            print(lista_jugadores[jugada].mano)
                            elegida=input("No existe esa ficha, porfavor tome una de sus opciones!\n")                
                        indice_ficha= int(elegida) - 1
                        ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                        
                contar_fichas_totales(ficha_elegida,mesita)
                lista_jugadores[jugada].mano.remove(ficha_elegida)
                mesita.juego.append(ficha_elegida)
                jugada+=1
                variable_pa_borrar=os.system('cls')
                continue
            if len(mesita.juego)==0 and partidas >0:
                print("{} Comienza con cualquier ficha ya que ganaste la pasada!!!\n".format(lista_jugadores[jugada].nombre))
                print(lista_jugadores[jugada].mano)
                elegida=input() 
                indice_ficha= int(elegida) - 1
                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                contar_fichas_totales(ficha_elegida,mesita)
                lista_jugadores[jugada].mano.remove(ficha_elegida)
                mesita.juego.append(ficha_elegida)
                jugada+=1
                variable_pa_borrar=os.system('cls')
                continue                
                
            if (mesita.juego[0][0] == mesita.juego[-1][-1]) and mesita.juego[0][0] == 0 and mesita.f0 == 7:
                input("{} Ha trancado el juego!\n".format(lista_jugadores[jugada-1].nombre))
                ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada],lista_jugadores)
                input ("El ganador del juego es: {} !!!\nSe lleva {} puntos !!!".format(ganador.nombre,sumar_puntos(lista_jugadores)))
                ganadora=True
                break
            if (mesita.juego[0][0] == mesita.juego[-1][-1]) and mesita.juego[0][0] == 1 and mesita.f1 == 7:
                input("{} Ha trancado el juego!\n".format(lista_jugadores[jugada-1].nombre))
                ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada],lista_jugadores)
                input ("El ganador del juego es: {} !!!\nSe lleva {} puntos !!!".format(ganador.nombre,sumar_puntos(lista_jugadores)))
                ganadora=True
                break     
            if (mesita.juego[0][0] == mesita.juego[-1][-1]) and mesita.juego[0][0] == 2 and mesita.f2 == 7:
                input("{} Ha trancado el juego!\n".format(lista_jugadores[jugada-1].nombre))
                ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada],lista_jugadores)
                input ("El ganador del juego es: {} !!!\nSe lleva {} puntos !!!".format(ganador.nombre,sumar_puntos(lista_jugadores)))
                break     
            if (mesita.juego[0][0] == mesita.juego[-1][-1]) and mesita.juego[0][0] == 3 and mesita.f3 == 7:
                input("{} Ha trancado el juego!\n".format(lista_jugadores[jugada-1].nombre))
                ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada],lista_jugadores)
                input ("El ganador del juego es: {} !!!\nSe lleva {} puntos !!!".format(ganador.nombre,sumar_puntos(lista_jugadores)))
                break     
            if (mesita.juego[0][0] == mesita.juego[-1][-1]) and mesita.juego[0][0] == 4 and mesita.f4 == 7:
                input("{} Ha trancado el juego!\n".format(lista_jugadores[jugada-1].nombre))
                ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada],lista_jugadores)
                input ("El ganador del juego es: {} !!!\nSe lleva {} puntos !!!".format(ganador.nombre,sumar_puntos(lista_jugadores)))
                break     
            if (mesita.juego[0][0] == mesita.juego[-1][-1]) and mesita.juego[0][0] == 5 and mesita.f5 == 7:
                input("{} Ha trancado el juego!\n".format(lista_jugadores[jugada-1].nombre))
                ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada],lista_jugadores)
                input ("El ganador del juego es: {} !!!\nSe lleva {} puntos !!!".format(ganador.nombre,sumar_puntos(lista_jugadores)))
                break     
            if (mesita.juego[0][0] == mesita.juego[-1][-1]) and mesita.juego[0][0] == 6 and mesita.f6 == 7:
                input("{} Ha trancado el juego!\n".format(lista_jugadores[jugada-1].nombre))
                ganador= contar_fichas_tranque(lista_jugadores[jugada-1],lista_jugadores[jugada],lista_jugadores)
                input ("El ganador del juego es: {} !!!\nSe lleva {} puntos !!!".format(ganador.nombre,sumar_puntos(lista_jugadores)))
                break         
            
            
            else:
                
                if validar_jugada(mesita.juego[0][0],mesita.juego[-1][-1],lista_jugadores[jugada].mano):
                    print("{} Seleccione su ficha\n".format(lista_jugadores[jugada].nombre))
                    print(lista_jugadores[jugada].mano)
                    elegida=input()
                    while  (int(elegida) -1) > len(lista_jugadores[jugada].mano)-1:
                        print(lista_jugadores[jugada].mano)
                        elegida=input("No existe esa ficha, porfavor tome una de sus opciones!\n")
                    indice_ficha= int(elegida) - 1
                    ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]
                    if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                        while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) == False:
                            print("Esta ficha no es valida, porfavor seleccione otra pieza")
                            print(mesita.juego)
                            print("{}:".format(lista_jugadores[jugada].nombre))
                            print(lista_jugadores[jugada].mano)                            
                            elegida=input()
                            indice_ficha= int(elegida) - 1
                            ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]            
                    
                    if  validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) and (mesita.juego[0][0] == mesita.juego[-1][-1]) :
                        choice=input("La desea en la izquierda o en la derecha?\nEscriba 'I' para la izquierda y 'D'para la derecha\n")
                        if choice == 'D':
                            if ficha_elegida[0] == mesita.juego[-1][-1]:
                                mesita.juego.append(ficha_elegida)
                            else:
                                mesita.juego.append(ficha_elegida[::-1])
                        if choice == 'I':
                            if ficha_elegida[-1] == mesita.juego[0][0]:                       
                                mesita.juego.insert(0,ficha_elegida)
                            else:
                                mesita.juego.insert(0,ficha_elegida[::-1])
                        contar_fichas_totales(ficha_elegida,mesita)
                        lista_jugadores[jugada].mano.remove(ficha_elegida)                                                                                                
                        if len(lista_jugadores[jugada].mano) == 0:
                            if (ficha_elegida[0] == mesita.juego[-1] and ficha_elegida[-1] == mesita.juego[0]) or (ficha_elegida[-1] == mesita.juego[-1] and ficha_elegida[0] == mesita.juego[0]):
                                input("Capicua!!! 25 puntos extra!!!\n")
                                capicua=True
                            input("{} Ha ganado el juego!,ya termino todas sus fichas!\nSe lleva {} puntos !!!".format(lista_jugadores[jugada].nombre,sumar_puntos(lista_jugadores,capicua)))
                            ganadora=True  
                            lista_jugadores[jugada].puntos=sumar_puntos(lista_jugadores,capicua)
                            
                            break
                        jugada+=1
                        variable_pa_borrar=os.system('cls')
                        continue
                    if validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) and (ficha_elegida[0] == ficha_elegida[1]):
                        if mesita.juego[0][0] == ficha_elegida[0]:
                            mesita.juego.insert(0,ficha_elegida)
                        if mesita.juego[-1][-1] == ficha_elegida[0]:
                            mesita.juego.append(ficha_elegida)
                        contar_fichas_totales(ficha_elegida,mesita)
                        lista_jugadores[jugada].mano.remove(ficha_elegida) 
                        if len(lista_jugadores[jugada].mano) == 0:
                            if (ficha_elegida[0] == mesita.juego[-1] and ficha_elegida[-1] == mesita.juego[0]) or (ficha_elegida[-1] == mesita.juego[-1] and ficha_elegida[0] == mesita.juego[0]):
                                input("Capicua!!! 25 puntos extra!!!\n")
                                capicua=True                            
                            input("{} Ha ganado el juego!,ya termino todas sus fichas!\nSe lleva {} puntos !!!".format(lista_jugadores[jugada].nombre,sumar_puntos(lista_jugadores,capicua)))
                            ganadora=True  
                            lista_jugadores[jugada].puntos=sumar_puntos(lista_jugadores,capicua)
                            
                            break
                        jugada+=1
                        variable_pa_borrar=os.system('cls')
                        continue
                    if validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) and (ficha_elegida[-1] == mesita.juego[0][0] or ficha_elegida[-1] == mesita.juego[-1][-1]) and (ficha_elegida[0] == mesita.juego[0][0] or ficha_elegida[0] == mesita.juego[-1][-1]):
                        choice=input("La desea en la izquierda o en la derecha?\nEscriba 'I' para la izquierda y 'D'para la derecha\n")
                        if choice == 'D':
                            if ficha_elegida[0] == mesita.juego[-1][-1]:
                                mesita.juego.append(ficha_elegida)
                            else:
                                mesita.juego.append(ficha_elegida[::-1])
                        if choice == 'I':
                            if ficha_elegida[-1] == mesita.juego[0][0]:                       
                                mesita.juego.insert(0,ficha_elegida)
                            else:
                                mesita.juego.insert(0,ficha_elegida[::-1])
                        contar_fichas_totales(ficha_elegida,mesita)
                        lista_jugadores[jugada].mano.remove(ficha_elegida)                                                                                                
                        if len(lista_jugadores[jugada].mano) == 0:
                            if (ficha_elegida[0] == mesita.juego[-1] and ficha_elegida[-1] == mesita.juego[0]) or (ficha_elegida[-1] == mesita.juego[-1] and ficha_elegida[0] == mesita.juego[0]):
                                input("Capicua!!! 25 puntos extra!!!\n")
                                capicua=True                            
                            input("{} Ha ganado el juego!,ya termino todas sus fichas!\nSe lleva {} puntos !!!".format(lista_jugadores[jugada].nombre,sumar_puntos(lista_jugadores,capicua)))
                            ganadora=True  
                            lista_jugadores[jugada].puntos=sumar_puntos(lista_jugadores,capicua)
                            
                            break
                        jugada+=1
                        variable_pa_borrar=os.system('cls')
                        continue                                                                                                                            
                    if validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) and mesita.juego[-1][-1] == ficha_elegida[1] :
                        if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                            while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) ==  False:
                                print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                                print(mesita.juego)
                                print("{}:".format(lista_jugadores[jugada].nombre))
                                print(lista_jugadores[jugada].mano)                            
                                elegida=input()
                                indice_ficha= int(elegida) - 1
                                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                      
                        contar_fichas_totales(ficha_elegida,mesita)
                        lista_jugadores[jugada].mano.remove(ficha_elegida)
                        mesita.juego.append(ficha_elegida[::-1])
                        if len(lista_jugadores[jugada].mano) == 0:
                            if (ficha_elegida[0] == mesita.juego[-1] and ficha_elegida[-1] == mesita.juego[0]) or (ficha_elegida[-1] == mesita.juego[-1] and ficha_elegida[0] == mesita.juego[0]):
                                input("Capicua!!! 25 puntos extra!!!\n")
                                capicua=True                            
                            input("{} Ha ganado el juego!,ya termino todas sus fichas!\nSe lleva {} puntos !!!".format(lista_jugadores[jugada].nombre,sumar_puntos(lista_jugadores,capicua)))
                            ganadora=True  
                            lista_jugadores[jugada].puntos=sumar_puntos(lista_jugadores,capicua)
                            
                            break
                        jugada+=1
                        variable_pa_borrar=os.system('cls')
                        continue                
                    if  validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) and mesita.juego[0][0] == ficha_elegida[1]:
                        if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                            while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) == False:
                                print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                                print(mesita.juego)
                                print("{}:".format(lista_jugadores[jugada].nombre))
                                print(lista_jugadores[jugada].mano)                            
                                elegida=input()
                                indice_ficha= int(elegida) - 1
                                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                      
        
                        contar_fichas_totales(ficha_elegida,mesita)
                        lista_jugadores[jugada].mano.remove(ficha_elegida) 
                        mesita.juego.insert(0,ficha_elegida) 
                        if len(lista_jugadores[jugada].mano) == 0:
                            if (ficha_elegida[0] == mesita.juego[-1] and ficha_elegida[-1] == mesita.juego[0]) or (ficha_elegida[-1] == mesita.juego[-1] and ficha_elegida[0] == mesita.juego[0]):
                                input("Capicua!!! 25 puntos extra!!!\n")
                                capicua=True                            
                            input("{} Ha ganado el juego!,ya termino todas sus fichas!\nSe lleva {} puntos !!!".format(lista_jugadores[jugada].nombre,sumar_puntos(lista_jugadores,capicua)))
                            ganadora=True  
                            lista_jugadores[jugada].puntos=sumar_puntos(lista_jugadores,capicua)
                            
                            break
                        jugada+=1
                        variable_pa_borrar=os.system('cls')
                        continue
                    if validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) and mesita.juego[0][0] == ficha_elegida[0]:
                        if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                            while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) == False:
                                print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                                print(mesita.juego)
                                print("{}:".format(lista_jugadores[jugada].nombre))
                                print(lista_jugadores[jugada].mano)                            
                                elegida=input()
                                indice_ficha= int(elegida) - 1
                                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                      
                        contar_fichas_totales(ficha_elegida,mesita)
                        lista_jugadores[jugada].mano.remove(ficha_elegida) 
                        mesita.juego.insert(0,ficha_elegida[::-1]) 
                        if len(lista_jugadores[jugada].mano) == 0:
                            if (ficha_elegida[0] == mesita.juego[-1] and ficha_elegida[-1] == mesita.juego[0]) or (ficha_elegida[-1] == mesita.juego[-1] and ficha_elegida[0] == mesita.juego[0]):
                                input("Capicua!!! 25 puntos extra!!!\n")
                                capicua=True                            
                            input("{} Ha ganado el juego!,ya termino todas sus fichas!\nSe lleva {} puntos !!!".format(lista_jugadores[jugada].nombre,sumar_puntos(lista_jugadores,capicua)))
                            ganadora=True  
                            lista_jugadores[jugada].puntos=sumar_puntos(lista_jugadores,capicua)
                            
                            break
                        jugada+=1
                        variable_pa_borrar=os.system('cls')
                        continue                
                    if validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) and mesita.juego[-1][-1] == ficha_elegida[0]:
                        if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                            while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) == False:
                                print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                                print(mesita.juego)
                                print("{}:".format(lista_jugadores[jugada].nombre))
                                print(lista_jugadores[jugada].mano)                            
                                elegida=input()
                                indice_ficha= int(elegida) - 1
                                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                      
                        contar_fichas_totales(ficha_elegida,mesita)
                        lista_jugadores[jugada].mano.remove(ficha_elegida) 
                        mesita.juego.append(ficha_elegida) 
                        if len(lista_jugadores[jugada].mano) == 0:
                            if (ficha_elegida[0] == mesita.juego[-1] and ficha_elegida[-1] == mesita.juego[0]) or (ficha_elegida[-1] == mesita.juego[-1] and ficha_elegida[0] == mesita.juego[0]):
                                input("Capicua!!! 25 puntos extra!!!\n")
                                capicua=True                            
                            input("{} Ha ganado el juego!,ya termino todas sus fichas!\nSe lleva {} puntos !!!".format(lista_jugadores[jugada].nombre,sumar_puntos(lista_jugadores,capicua)))
                            ganadora=True  
                            lista_jugadores[jugada].puntos=sumar_puntos(lista_jugadores,capicua)
                            
                            break
                        jugada+=1
                        variable_pa_borrar=os.system('cls')
                        continue 
                    if validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) and mesita.juego[-1][-1] == ficha_elegida[-1]:
                        if not validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida):
                            while validar_pieza(mesita.juego[0][0],mesita.juego[-1][-1],ficha_elegida) == False:
                                print("Esta ficha no es valida, porfavor seleccione otra pieza\n")
                                print(mesita.juego)
                                print("{}:".format(lista_jugadores[jugada].nombre))
                                print(lista_jugadores[jugada].mano)                            
                                elegida=input()
                                indice_ficha= int(elegida) - 1
                                ficha_elegida=lista_jugadores[jugada].mano[indice_ficha]                      
                        contar_fichas_totales(ficha_elegida,mesita)
                        lista_jugadores[jugada].mano.remove(ficha_elegida) 
                        mesita.juego.append(ficha_elegida[::-1]) 
                        if len(lista_jugadores[jugada].mano) == 0:
                            if (ficha_elegida[0] == mesita.juego[-1] and ficha_elegida[-1] == mesita.juego[0]) or (ficha_elegida[-1] == mesita.juego[-1] and ficha_elegida[0] == mesita.juego[0]):
                                input("Capicua!!! 25 puntos extra!!!\n")
                                capicua=True                            
                            input("{} Ha ganado el juego!,ya termino todas sus fichas!\nSe lleva {} puntos !!!".format(lista_jugadores[jugada].nombre,sumar_puntos(lista_jugadores,capicua)))
                            ganadora=True  
                            lista_jugadores[jugada].puntos=sumar_puntos(lista_jugadores,capicua)
                            
                            break
                        jugada+=1
                        variable_pa_borrar=os.system('cls')
                        continue                          
                                    
                else:
                    print("{} no tiene fichas disponibles!\n".format(lista_jugadores[jugada].nombre))
                    print(lista_jugadores[jugada].mano)
                    input()
                    jugada+=1
                    variable_pa_borrar=os.system('cls')
                    continue
        partidas+=1
game()    
    




    
