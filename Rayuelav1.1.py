def escogerJugador():

#realizamos el menu correspondiente a la cantidad de jugadores en este caso 2
    if(cantidadJugadores==2):
#Presentamos los jugadores en juego
        print("Ingrese el jugador que jugara este turno ")
        print("escoge a o 1 para:  Jugador A o 1")
        print("escoge b o 2 para:  Jugador B o 2")
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
        print("escoge a o 1 para:  Jugador A o 1")
        print("escoge b o 2 para:  Jugador B o 2")
        print("escoge c o 3 para:  Jugador C o 3")
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
        print("escoge a o 1 para:  Jugador A o 1")
        print("escoge b o 2 para:  Jugador B o 2")
        print("escoge c o 3 para:  Jugador C o 3")
        print("escoge d o 4 para:  Jugador D o 4")
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
# inicializamos a jugador con el jugador escogido
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
        print("el jugador "+ jugador + " perdido su turno " )
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

def lee_entero():
    """
    En esta funcion se hacen las validaciones para poder escribir solo enteros al momento de ingresar el numero de jugadores
    Parametros:
    -------------------
        enteros
    Retorna:
    -------------------
        cantidadJugadores : int
            nos ayuda a saber el numero de jugadores que se ingresaran.
"""
    #hasta colocar la cantidad de jugadores validos en numeros
    while True:
        #Comenzamos el juego
        print("\n<<<<<<<JUEGO TRADICIONAL LA RAYUELA>>>>>>>\n")
        #repetimos el juego 
        cantidadJugadores = input("Escribe un numero entero del 2 al 4: ")
        try:
            cantidadJugadores = int(cantidadJugadores)
            return cantidadJugadores
        except ValueError:
           print ("La entrada es incorrecta escribe un numero entero")

# funcion principal del juego
if __name__ == '__main__':
#Declaramos una variable global
    cantidadJugadores= lee_entero()
#Comenzamos el juego
    print("\n<<<<<<<JUEGO TRADICIONAL LA RAYUELA>>>>>>>\n")
#Si la cantidad de jugadores que el usario desea crear esta fuera del rango permitido se repetira el ingreso
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