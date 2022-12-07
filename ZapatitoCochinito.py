'''

Zapatito cochinito, es un juego tradicional en la  poblacion ecuatoriana, consiste en un grupo de jugadores que debe se minimo de 2 jugadores hasta un maximo de 5 jugadores
los cuales todos juntan un pie y se comienza a contar el la estrofa particular de este juego el cual se va contando al ritmo de la cancion los pies de los jugadores,
a la ultima persona en ser contada debera cambiar de pie y si ya lo hizo anteriormente entonces sale del juego, el ultimo jugador en quedar en la partida es quien gana

Autor:
Brandon Arellano

Version: 1.0
'''
def caratula(): 
    '''
    Es una funcion el cual realiza la caratula del juego y hace una prueba escritorio de la cantidad de jugadores que ingresa el usuario, el cual no debe ser menor que 2 y
    mayor que 4
    Parametros:
    -----------
        No tiene parametros de entrada 
    Retorna:
    -----------
        Retorna un numero entero
    '''
    #Se imprime la caratula de Bienvenida al juego
    print("\n","-"*25, "Bienvenido a Zapatito Cochinito","-"*25) 
    #Imprime indicaciones sobre la cantidad de numero de jugadores 
    print("Al ingresar el numero de jugadores este debe ser minimo de 2 y maximo de 4 jugadores")
    #A la variable numeroJugadores se le asigna el valor de un numero entero que se le solicita al usuario para la cantidad de jugadores 
    numeroJugadores= input ("\nIngresa el numero de Jugadores: ")
    validacion=True
    
    while validacion == True:
        if numeroJugadores.isalpha():
            numeroJugadores=input('Has ingresado una letra, por favor ingresa un numero del 2 al 4: ')
            validacion= True
            
        else: 
            validacion= False
    numeroJugadores = int (numeroJugadores)
    #Se crea un ciclo repetitivo while para la validacion de que el valor debe ser mayor que 1
    while numeroJugadores<2 :
        #implime si no se cumple la funcion while 
        print("No puede ser numeros menores que 2")
        #Se le vuelve a pedir al usuario que ingrese nuevamente la cantidad de jugadores
        numeroJugadores = int(input("Ingresa nuevamente el numero de Jugadores: "))
    #Se crea un ciclo repetitivo while para la validacion de que el valor no sea mayor que 4
    while numeroJugadores>4:
        #imprime de que no puede ser mayor que 4
        print("No puede ser numeros mayores que 4")
        #Se le vuelve a pedir al usuario que ingrese nuevamente la cantidad de jugadores 
        numeroJugadores = int(input("Ingresa nuevamente el numero de Jugadores: "))

    #Se imprime el numero de jugadores
    print("\nHas ingresado "+ str (numeroJugadores) +" jugadores")
    #imprime que se esta comenzando el juego 
    print("Que comience el juego ")
    #Empieza la estrofa particular del juego
    print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
    #retorna el valor del numero de jugadores 
    return (numeroJugadores)

def jugadoresParticipan(numeroJugadores):
    '''
    Es una funcion el cual de acuerdo al numero de jugadores, por medio de las funciones if se filtra, se toma una u otra opcion,
    se crea un vector de acuerdo a al numero de jugadores
    Parametros:
    -----------
        Se envia el numero de jugadores que fueron ingresados por el usuario
    Retorna:
    -----------
        retorna el vector jugadores
    '''
    #imprime los jugadores participantes
    print('Jugadores participantes: ')
    #por medio de un if se filtra y se crea el vector jugadores con la cantidad de jugadores 
    if numeroJugadores == 2:
        #se cre al vector con 2 jugadores
        jugadores= ['jugador1', 'jugador2']
        #imprime vetor jugadores 
        print (jugadores)
    #por medio de un if se filtra y se crea el vector jugadores con la cantidad de jugadores
    elif numeroJugadores == 3:
        #se cre al vector con 3 jugadores
        jugadores= ['jugador1', 'jugador2', 'jugador3']
        #imprime vetor jugadores
        print (jugadores)
    #por medio de un if se filtra y se crea el vector jugadores con la cantidad de jugadores
    elif numeroJugadores == 4:
        #se cre al vector con 4 jugadores
        jugadores= ['jugador1', 'jugador2','jugador3','jugador4']
        #imprime vetor jugadores
        print (jugadores)
    #retorna el vector con los jugadores
    return jugadores

def contar(jugadores):
    '''
    Es el procedimiento el cual cuenta a los jugadores y establece a los ganadores 
    Parametros:
    -----------
        Se le envia el vector de jugadores 
    Retorna:
    ----------
        No retorna nada 
    '''
    #Es un if que filtra, para el vector de 2 jugadores 
    if jugadores == ['jugador1', 'jugador2']:
        #imprime que el jugador debe cambiar de pie
        print('jugador 2 cambia de pie ')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador debe cambiar de pie
        print ('jugador 1 cambia de pie ')
        #imprime que al jugador que ha ganado
        print('Gana jugador 1')
    elif jugadores == ['jugador1', 'jugador2', 'jugador3']:
        #imprime que el jugador debe cambiar de pie
        print('jugador 3 cambia de pie')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador debe cambiar de pie
        print('jugador 2 cambia de pie')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador debe cambiar de pie
        print('jugador 1 cambia de pie ')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador salio del juego
        print('jugador 3 sale' )
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador salio del juego
        print('jugador 1 sale' )
        #imprime que al jugador que ha ganado
        print('Gana jugador 2')
    elif jugadores == ['jugador1', 'jugador2','jugador3','jugador4']:
        #imprime que el jugador debe cambiar de pie
        print('jugador 4 cambia de pie')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador debe cambiar de pie
        print('jugador 3 cambia de pie')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador debe cambiar de pie
        print('jugador 2 cambia de pie')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador debe cambiar de pie
        print('jugador 1 cambia de pie')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador salio del juego
        print('jugador 4 sale' )
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador salio del juego       
        print('jugador 2 sale')
        #Se vuelve a cantar 
        print("Zapa-tito cochi-nito, cam-bia de pie-ci-to, pero mi burrito dijo que me-jor lo cambiarias tu, nadie mas que tu !")
        #imprime que el jugador salio del juego
        print('jugador 3 sale')
        #imprime que al jugador que ha ganado
        print('Gana el jugador 1')
        

def despedida ():
    '''
    Es una funcion el cual imprime el cierre del programa
    Parametros:
    -----------
        No tiene parametros de entrada 
    Retorna:
    ----------
        No retorna nada 
    '''
    #imprime la caratula de despedida
    print('*'*38)
    print('gracias por jugar a Zapatito Cochinito')
    print('*'*38)


if __name__ == '__main__':
    ''''
    Funcion principal de main, hace el llamado de las funciones 
    '''
    #inicializa las variables 
    numeroJugadores=0
    jugadores=[" "]
    #se le asigna el valor que retorna la funcion caratula
    numeroJugadores = caratula()
    #asgina el valor de la funcion 
    jugadores=jugadoresParticipan(numeroJugadores)
    #llama a la funcion y manda un parametro
    contar(jugadores)
    #llama a la funcoin de despedida 
    despedida()
