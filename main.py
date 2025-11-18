import funciones
import os
import random
import numpy as np
#from tablero import Tablero
#from jugador import Jugador, IA
#from funciones import ejecutar_partida
from Clases.Tablero import Tablero
from Clases.Jugador import Jugador
from variables import *
print("Iniciando juego de Hundir la Flota")

jugador = Jugador()
ia = Jugador()

#jugador.ponerBarcosEnTablero()
#ia.ponerBarcosEnTablero()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_victoria(jugador_rival):
    # Cuenta los barcos (O) que quedan en el tablero oculto del rival
    return np.count_nonzero(jugador_rival.tablero_oculto.tablero == "O") == 0

def obtener_disparo_humano():
    while True:
        try:
            fila = int(input(f"Fila ({0}-{ALTURA_TABLERO-1}): "))
            columna = int(input(f"Columna ({0}-{BASE_TABLERO-1}): "))
            
            if 0 <= fila < ALTURA_TABLERO and 0 <= columna < BASE_TABLERO:
                return (fila, columna)
            else:
                print("Coordenadas fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Introduce solo números.")


if __name__ == "__main__":
    print("INICIANDO EL JUEGO DE BATALLA NAVAL")
    
    jugador = Jugador()
    ia = Jugador()
    
    print("\n[PREPARACIÓN] Colocando barcos del Jugador...")
    jugador.ponerBarcosEnTablero()
    print("\n[PREPARACIÓN] Colocando barcos de la IA...")
    ia.ponerBarcosEnTablero()
    
    input("\nPresiona ENTER para comenzar la batalla...")
    
    turno = 1
    
    # --- BUCLE DE BATALLA ---
    while not verificar_victoria(jugador) and not verificar_victoria(ia):
        clear_screen()
        print(f"================== RONDA {turno} ==================")
        
        # 1. TURNO DEL JUGADOR HUMANO
        print(f"\n[TU TURNO] Dispara a las coordenadas del rival (Tablero de Seguimiento):")
        jugador.tablero.imprimirTablero()
        
        coordenadas_disparo = obtener_disparo_humano()
        
        jugador.disparar(ia, coordenadas_disparo) 
        
        if verificar_victoria(ia):
            print("\n¡VICTORIA! Todos los barcos de la IA han sido hundidos.")
            break

        print("-" * 30)
        
        # 2. TURNO DE LA IA
        print(f"\n[TURNO DE LA IA] La IA está disparando...")
        ia.disparar(jugador) 
        
        print("\nAsí quedó tu tablero:")
        jugador.tablero_oculto.imprimirTablero()
        
        if verificar_victoria(jugador):
            print("\n¡DERROTA! La IA hundió todos tus barcos.")
            break

        input("\nPresiona ENTER para el siguiente turno...")
        turno += 1

    print("\n================ FIN DE LA PARTIDA ===============")