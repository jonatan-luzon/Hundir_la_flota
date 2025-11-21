import funciones as f
import random
from Clases.Tablero import Tablero
from Clases.Jugador import Jugador
from variables import *

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
    while True:
        f.clear_screen()
        print(f"================== RONDA {turno} ==================")
        
        # 1. TURNO DEL JUGADOR HUMANO
        print(f"\n[TU TURNO] Dispara a las coordenadas del rival (Tablero de Seguimiento):")
        jugador.tablero.imprimirTablero()
        
        pasar_turno = False
        while not pasar_turno:

            coordenadas_disparo = jugador.obtener_disparo_humano()
            #coordenadas_disparo = None #si quieres randomizar una partida comenta la linea anterior y descomenta esta
            pasar_turno = jugador.disparar(ia, coordenadas_disparo)
            jugador.tablero.imprimirTablero()
            jugador.tablero_oculto.imprimirTablero()

        if f.verificar_victoria(ia):
            print("\n¡VICTORIA! Todos los barcos de la IA han sido hundidos.")
            break

        print("-" * 30)
        
        # 2. TURNO DE LA IA
        print(f"\n[TURNO DE LA IA] La IA está disparando...")

        pasar_turno = False
        while not pasar_turno:
            pasar_turno = ia.disparar(jugador) 
        
        print("\nAsí quedó tu tablero:")
        jugador.tablero_oculto.imprimirTablero()
        
        if f.verificar_victoria(jugador):
            print("\n¡DERROTA! La IA hundió todos tus barcos.")
            break

        input("\nPresiona ENTER para el siguiente turno...")
        turno += 1

    print("\n================ FIN DE LA PARTIDA ===============")