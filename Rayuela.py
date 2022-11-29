"""
JUEGO TRADICIONAL DE LA RAYUELA
La rayuela consiste en un juego el cual participan de 2 a 4 personas
en este juego las instrucciones son muy simples 
la primera regla es que la piedra caiga dentro de los cuadros a saltar
si la piedra cae en la parte de afuera el jugador a perdido su turno
la segunda es que si la piedra cae adentro el jugador debe saltar todos los cuadros en orden
y al regreso debe recoger la piedra
si la piedra cae afuera pasa al siguiente jugador y el que la lanzo pierde su turno
"""

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
            valor contiene a los jugadores que realizaron e juego

    """
    #realizamos el menu correspondiente a la cantidad de jugadores en este caso 2
    if(cantidadJugadores==2):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que jugara este turno ")
        print("escoge a para:  Jugador A")
        print("escoge b para:  Jugador B")
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
        print("Ingrese el jugador que jugara este turno ")
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
        print("Ingrese el jugador que jugara este turno ")
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

def rayuela():
    """
    Es una funcion la cual utiliza la variable global "rayuela", para poder ingresar los datos que cada concursante realizo
    con la posicion de la piedra la cual seria si es adentro o afuera
    Parametros:
    ----------------
        no tiene parametros de entrada

    Retorna:
    ----------------
        posicion: int
            contiene dos enteros para saber la posicion de la piedra
                1: adentro, 2: afuera
    """
# inicializamosm a jugador con el jugador escogido
    jugador = escogerJugador()
    #imprimimos el jugador escogido
    print ("jugador: " + jugador)
    #inicializamos la posicion de la piedra
    posicion = 2
    #damos las opciones a elegir al juez
    print ("opcion 1: adentro")
    print ("opcion 2: afuera ")
    #ingresamos en que posicion cayo la piedra adentro que es 1 o afuera que es 2
    posicion = int (input ("La piedra cayo adentro o afuera?  " '\n'))
    # comparamos si la piedra cayo en la parte de afuera
    if posicion == 2:
        #imprimimos el mensaje de que el jugador pierde el turno
        print("el jugador "+ jugador + " perdido su turno " '\n')
        #llamamos a la funcion escoger jugador y rayuela para hacer una repeticion y seguir conotro jugador
        escogerJugador()
        rayuela()
    # comparamos si la piedra cayo en la parte de adentro
    if posicion == 1:
        #imprimimos el mensaje de que el jugador puede seguir jugando hasta terminar el juego recogiendo la piedra que lanzo
        print("el jugador " + jugador + " sigue jugando y saltara hasta el final recogiendo su piedra ")
        escogerJugador()
        rayuela()
    #retornamos el valor de posicion 
    return posicion 

# funcion principal del juego
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
            rayuela()

