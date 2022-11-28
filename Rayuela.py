from random import *

def escogerJugador():
    """
    Es una funcion la cual utiliza la variable global "cantidadJugadores", para utilizar el menu correspondiente
    con la cantidad de jugadores
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        jugadorEscogido : string
            valor contiene el jugador que realizo primero el reto

    """
    #realizamos el menu correspondiente a la cantidad de jugadores en este caso 2
    if(cantidadJugadores==2):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que jugara primero ")
        print("escoge a para:  Jugador A")
        print("escoge a para:  Jugador B")
        #ingresamos el jugador que que jugara primero
        jugadorEscogido=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(jugadorEscogido.lower()>'b'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
     #realizamos el menu correspondiente a la cantidad de jugadores en este caso 3
    elif(cantidadJugadores==3):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que jugara primero ")
        print("escoge a para:  Jugador A")
        print("escoge b para:  Jugador B")
        print("escoge c para:  Jugador C")
        #ingresamos el jugador que que jugara primero
        jugadorEscogido=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(jugadorEscogido.lower()>'c'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
    #realizamos el menu correspondiente a la cantidad de jugadores en este caso 4
    elif(cantidadJugadores==4):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que jugara primero ")
        print("escoge a para:  Jugador A")
        print("escoge b para:  Jugador B")
        print("escoge c para:  Jugador C")
        print("escoge d para:  Jugador D")
        #ingresamos el jugador que que jugara primero
        jugadorEscogido=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido
        #lower convierte las letras a minusculas
        if(jugadorEscogido.lower()>'d'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
    return jugadorEscogido

def rayuela(jugador):
    print ("jugador: " + jugador)
    posicion = 2
    while (posicion != 1):
        print ("opcion 1: adentro")
        print ("opcion 2: afuera ")
        posicion = int (input ("Piedra adentro o afuera?  "))
        print ("La piedra del jugador cayo en la parte de adentro")

def ronda():
    
    jugador1 = 0
    jugador2 = 0
    jugador3 = 0
    jugador4 = 0
    contador = 0
    while(contador <= 10 ):
        #rayuela(jugadorGlobal)
        jugadorGlobal = escogerJugador()
        
        if (jugadorGlobal == 'a'):
            jugador1 += 1
            if(jugador1 == 10):
                print("El jugador a ha ganado")
                break
        elif (jugadorGlobal == 'b'):
            jugador2 += 1
            if(jugador2 == 10):
                print("El jugador b ha ganado")
                break
        elif (jugadorGlobal == 'c'):
            jugador3 += 1
            if(jugador3 == 10):
                print("El jugador c ha ganado")
                break
        elif (jugadorGlobal == 'd'):
            jugador4 += 1
            if(jugador4 == 10):
                print("El jugador d ha ganado")
                break
    contador = contador + 1


if __name__ == '__main__':
    #Declaramos una variable global
    cantidadJugadores=0
    #Comenzamos el juego
    print("\n<<<<<<<JUEGO TRADICIONAL LA RAYUELA>>>>>>>\n")
    #Si la cantidad de jugadores que el usario desea crear esta fuera del rango permitido se repetira el ingre
    #hasta colocar la cantidad de jugadores validos
    while(cantidadJugadores > 4 or cantidadJugadores <2 ):
        #Presenta al usuario la cantidad de jugadores permitidos
        print("Jugadores permitidos de 2 a 4")
        #Ingreso de la cantidad de jugadores 
        cantidadJugadores=int(input("Ingrese la cantidad de jugadores: "))
        #Comparamos si los jugadores estan entre 2 y 4
        if(cantidadJugadores>4 or cantidadJugadores<2):
            print("Catidad de jugadores invalidos\n")
        else:
            ronda()