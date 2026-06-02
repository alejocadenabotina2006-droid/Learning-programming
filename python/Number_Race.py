import random

cantidad_jugadores = 0
limite_tablero = 0
casillas = []
contador_dobles = []
fin_juego = False


def solicitar_jugadores():
    num = int(input("Digite la cantidad de participantes (2 a 4): "))

    while num < 2 or num > 4:
        num = int(input("Valor inválido. Ingrese entre 2 y 4 jugadores: "))

    return num


def seleccionar_nivel():
    print("\n1. Tablero de 20 casillas")
    print("2. Tablero de 30 casillas")
    print("3. Tablero de 50 casillas")
    print("4. Tablero de 100 casillas")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        return 20
    elif opcion == 2:
        return 30
    elif opcion == 3:
        return 50
    else:
        return 100


def tirar_dados():
    valor1 = random.randint(1, 6)
    valor2 = random.randint(1, 6)

    return valor1, valor2


def iniciar_juego():
    jugadores = solicitar_jugadores()
    meta = seleccionar_nivel()

    casillas = [0] * jugadores
    contador_dobles = [0] * jugadores

    terminado = False

    while not terminado:

        for jugador in range(jugadores):

            print(f"\nTurno del jugador {jugador + 1}")

            dado_a, dado_b = tirar_dados()

            print("Primer dado:", dado_a)
            print("Segundo dado:", dado_b)

            if dado_a == dado_b:
                contador_dobles[jugador] += 1
            else:
                contador_dobles[jugador] = 0

            if contador_dobles[jugador] == 3:
                print(f"¡El jugador {jugador + 1} gana al obtener tres dobles consecutivos!")
                terminado = True
                break

            movimiento = dado_a + dado_b
            casillas[jugador] += movimiento

            print("Posición actual:", casillas[jugador])

            if casillas[jugador] >= meta:
                print(f"¡El jugador {jugador + 1} alcanzó la meta y ganó la partida!")
                terminado = True
                break


iniciar_juego()
