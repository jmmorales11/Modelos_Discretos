"""
Simon dice, es un juego tradicional, consiste en en grupo de jugadores minimo 2 y maximo 5 
los cuales deben ir acumulando puntos en 5 rondas, al final se muestra al jugador ganador con mas puntos realizados

Autores:
Jeimy Marley Morales Sosa

Verisión:
VER.1.2
"""
def simonDice():
    """
    Es un procedimiento que nos muestra en que ronda de juego estan los jugadores, asignar puntos al jugador el
    cual realizo el reto, y escoger el jugador con mayor puntos acumulados
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    #Declaracion de un contador ronda, el cual va sumar 1 por cad ronda
    ronda=1
    #Declaracion de la variable ganador la cual va a guardar el maximo de puntos de un jugador
    ganador=0
    #Declaracion de los 5 jugadores 
    jugadorA=0
    jugadorB=0
    jugadorC=0
    jugadorD=0
    jugadorE=0
    #Comienza las rondas de juego hasta que la ronda sea 5
    while ronda<=5:
        #Imprime la ronda en la que se encuentran los jugadores con las rondas maximas
        print("Ronda  ", ronda," de ",5)
        #Imprime el reto que debe realizar
        print("\n-----------\nSimon dice  ",reto())
        #En la variable jugador se guarda el valor de retorno de la funcion escoger Jugador la cual es un letra
        jugador=escogerJugador()
        #Comparamos el jugador escogido con el jugador A
        if(jugador == 'a'or jugador == 'A'):
            #Si el jugador A realizo el reto se acumula un pundo adicional a jugador A
            jugadorA+=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador A realizo el reto tiene ",jugadorA," puntos")
        #Comparamos el jugador escogido con el jugador B
        elif (jugador=='b'or jugador == 'B'):
            #Si el jugador B realizo el reto se acumula un pundo adicional a jugador B
            jugadorB +=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador B realizo el reto tiene ",jugadorB," puntos")
        #Comparamos el jugador escogido con el jugador C
        elif (jugador=='c' or jugador == 'C'):
            #Si el jugador C realizo el reto se acumula un pundo adicional a jugador C
            jugadorC +=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador C realizo el reto tiene ",jugadorC," puntos")
        #Comparamos el jugador escogido con el jugador D
        elif (jugador=='d'or jugador == 'D'):
            #Si el jugador D realizo el reto se acumula un pundo adicional a jugador D
            jugadorD +=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador D realizo el reto tiene ",jugadorD," puntos")
        #Comparamos el jugador escogido con el jugador E
        elif (jugador=='e' or jugador == 'E'):
            #Si el jugador E realizo el reto se acumula un pundo adicional a jugador E
            jugadorE +=1
            #Imprime el mensaje del jugador al cual se le añade un punto
            print("Jugador E realizo el reto tiene ",jugadorE," puntos")
        ronda +=1
    #Compardamos si el jugador A es mayor al ganador
    if(jugadorA>ganador ):
        #En la variable ganador se guarda el valor del Jugador A
        ganador=jugadorA
    #Compardamos si el jugador B es mayor al ganador
    if(jugadorB>ganador):
        #En la variable ganador se guarda el valor del Jugador B
        ganador=jugadorB
    #Compardamos si el jugador C es mayor al ganador
    if(jugadorC>ganador):
        #En la variable ganador se guarda el valor del Jugador C
        ganador=jugadorC
    #Compardamos si el jugador D es mayor al ganador
    if(jugadorD>ganador):
        #En la variable ganador se guarda el valor del Jugador D
        ganador=jugadorD
    #Compardamos si el jugador E es mayor al ganador
    if (jugadorE>ganador):
        #En la variable ganador se guarda el valor del Jugador E
        ganador=jugadorE
    #Utilizamos el proceso ganadorJuego, para imprimir el ganador del juego
    ganadorJuego(ganador,jugadorA,jugadorB,jugadorC,jugadorD,jugadorE)

def reto():
    """
    Es una funcion la cual nos permite ingresar el reto que el jugador debe realizar
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        reto : string
            valor que contiene el reto el cual debe realizar los jugadores

    """
    #Ingreso del reto el cual los jugadores deben realizar
    reto=input("Ingrese el reto que los jugadores deben realizar: ")
    #retornamos el reto
    return reto


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
    #comparamos la variable global con 2 para presentar el menu correspondiente a la cantidad de jugadores
    if(cantidadJugadores==2):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que realizo primero la orden")
        print("[a]  Jugador A")
        print("[b]  Jugador B")
        #ingresamos el jugador que realizo primero el reto
        jugadorEscogido=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(jugadorEscogido.lower()>'b'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
     #comparamos la variable global con 3 para presentar el menu correspondiente a la cantidad de jugadores
    elif(cantidadJugadores==3):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que realizo primero la orden")
        print("[a]  Jugador A")
        print("[b]  Jugador B")
        print("[c]  Jugador C")
        #ingresamos el jugador que realizo primero el reto
        jugadorEscogido=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(jugadorEscogido.lower()>'c'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
    #comparamos la variable global con 4 para presentar el menu correspondiente a la cantidad de jugadores
    elif(cantidadJugadores==4):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que realizo primero la orden")
        print("[a]  Jugador A")
        print("[b]  Jugador B")
        print("[c]  Jugador C")
        print("[d]  Jugador D")
        #ingresamos el jugador que realizo primero el reto
        jugadorEscogido=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(jugadorEscogido.lower()>'d'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
    #comparamos la variable global con 5 para presentar el menu correspondiente a la cantidad de jugadores
    elif(cantidadJugadores==5):
        #Presentamos los jugadores en juego
        print("Ingrese el jugador que realizo primero la orden")
        print("[a]  Jugador A")
        print("[b]  Jugador B")
        print("[c]  Jugador C")
        print("[d]  Jugador D")
        print("[e]  Jugador E")
        #ingresamos el jugador que realizo primero el reto
        jugadorEscogido=input("Seleccione:  ")
        #comparamos si el jugador esta dentro del rango permitido 
        #lower convierte las letras a minusculas
        if(jugadorEscogido.lower()>'e'):
            #si el jugador no esta dentro del rango se prensenta el mensaje
            print("Jugador no valido")
            #Regresamos a la misma funcion
            return escogerJugador()
    #Retornamos el jugador escogido
    return jugadorEscogido

def ganadorJuego(ganador,jugadorA,jugadorB,jugadorC,jugadorD,jugadorE ):
    """
    Es un proceso, el cual compara el valor maximo de puntos echos por un jugador con los puntos
    de cada jugador, para presentar al jugador ganador
    Parametros:
    ------------
        ganador : int 
            valor que contiene el maximo de puntos echos por un jugador
        jugadorA : int
            valor que contiene los puntso echos por el jugador A
        jugadorB : int
            valor que contiene los puntso echos por el jugador B
        jugadorC : int
            valor que contiene los puntso echos por el jugador C
        jugadorD : int
            valor que contiene los puntso echos por el jugador D
        jugadorE : 
            valor que contiene los puntso echos por el jugador E
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n----------------Felicidades---------------------")
    #Comparamos el valor ganador con el valor del jugador A
    if(jugadorA==ganador ):
        #Si el valor del ganador es igual valor del jugador A se presenta el mensaje con lo puntos del jugador A
        print("El ganador es el jugador A  con ",jugadorA," Puntos" )
    #Comparamos el valor ganador con el valor del jugador B
    elif(jugadorB==ganador):
        #Si el valor del ganador es igual valor del jugador B se presenta el mensaje con lo puntos del jugador B
        print("El ganador es el jugador B  con ",jugadorB," Puntos" )
     #Comparamos el valor ganador con el valor del jugador C
    elif(jugadorC==ganador):
        #Si el valor del ganador es igual valor del jugador C se presenta el mensaje con lo puntos del jugador C
        print("El ganador es el jugador C  con ",jugadorC," Puntos" )
    #Comparamos el valor ganador con el valor del jugador D
    elif(jugadorD==ganador):
        #Si el valor del ganador es igual valor del jugador D se presenta el mensaje con lo puntos del jugador D
        print("El ganador es el jugador D  con ",jugadorD," Puntos" )
    #Comparamos el valor ganador con el valor del jugador E  
    elif (jugadorE==ganador):
        #Si el valor del ganador es igual valor del jugador E se presenta el mensaje con lo puntos del jugador E
        print("El ganador es el jugador E  con ",jugadorE," Puntos" )

    
if __name__ == '__main__':
    #Declaramos una variable global
    cantidadJugadores=0
    #Comenzamos el juego
    print("\n<<<<<<<JUEGO TRADICIONAL SIMON DICE>>>>>>>\n")
    #Si la cantidad de jugadores que el usario desea crear esta fuera del rango permitido se repetira el ingre
    #hasta colocar la cantidad de jugadores validos
    while(cantidadJugadores > 5 or cantidadJugadores <2 ):
        #Presenta al usuario la cantidad de jugadores permitidos
        print("Jugadores permitidos de 2 a 5")
        #Ingreso de la cantidad de jugadores 
        cantidadJugadores=int(input("Ingrese la cantidad de jugadores: "))
        #Comparamos si los jugadores estan entre 2 y 5
        if(cantidadJugadores>5 or cantidadJugadores<2):
            print("Catidad de jugadores invalidos\n")
        else:
            #llamado al proceso
            simonDice()

        
