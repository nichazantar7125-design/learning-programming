import random

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def carrera_numerica():
    # Solicitar número de jugadores
    jugadores = int(input("Ingrese cantidad de jugadores (2-4): "))
    while jugadores < 2 or jugadores > 4:
        jugadores = int(input("Número inválido. Ingrese entre 2 y 4 jugadores: "))
    
    # Selección de nivel
    print("Seleccione nivel de tablero:")
    print("1. Básico (20 posiciones)")
    print("2. Intermedio (30 posiciones)")
    print("3. Avanzado (50 posiciones)")
    print("4. Experto (100 posiciones)")
    
    niveles = {1:20, 2:30, 3:50, 4:100}
    nivel = int(input("Nivel: "))
    while nivel not in niveles:
        nivel = int(input("Nivel inválido. Ingrese 1-4: "))
    
    meta = niveles[nivel]
    posiciones = [0] * jugadores
    consecutivos = [0] * jugadores
    
    ganador = None
    
    # Ciclo del juego
    while ganador is None:
        for i in range(jugadores):
            dado1, dado2 = lanzar_dados()
            print(f"\nJugador {i+1} lanzó {dado1} y {dado2}")
            
            if dado1 == dado2:
                consecutivos[i] += 1
            else:
                consecutivos[i] = 0
            
            if consecutivos[i] == 3:
                ganador = i
                print(f"Jugador {i+1} gana por tres dados iguales consecutivos!")
                break
            
            posiciones[i] += dado1 + dado2
            print(f"Jugador {i+1} avanza a posición {posiciones[i]}")
            
            # Nueva regla: choque de jugadores
            for j in range(jugadores):
                if j != i and posiciones[i] == posiciones[j]:
                    print(f"Jugador {i+1} cayó en la misma posición que Jugador {j+1}.")
                    print(f"Jugador {j+1} regresa al inicio!")
                    posiciones[j] = 0
            
            if posiciones[i] >= meta:
                ganador = i
                print(f"Jugador {i+1} llega a la meta y gana!")
                break
    
    print(f"\n🎉 El ganador es el Jugador {ganador+1} 🎉")

# Ejecutar juego
carrera_numerica()

