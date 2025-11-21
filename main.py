import funciones as f
import random
from Clases.Tablero import Tablero
from Clases.Jugador import Jugador
from variables import *

if __name__ == "__main__":
    print("INICIANDO EL JUEGO DE BATALLA NAVAL")
    
    # 1. INICIALIZACIÓN DE JUGADORES
    
    # Crea una instancia para el jugador humano.
    jugador = Jugador()
    # Crea una instancia para el oponente de la IA.
    ia = Jugador()
    
    # 2. PREPARACIÓN DEL TABLERO
    
    print("\n[PREPARACIÓN] Colocando barcos del Jugador...")
    # Llama al método para que el jugador coloque sus barcos (puede ser manual o aleatorio).
    jugador.ponerBarcosEnTablero()
    
    print("\n[PREPARACIÓN] Colocando barcos de la IA...")
    # Llama al método para que la IA coloque sus barcos (generalmente aleatorio).
    ia.ponerBarcosEnTablero()
    
    # Pausa antes de empezar la partida.
    input("\nPresiona ENTER para comenzar la batalla...")
    
    turno = 1
    
    # --- BUCLE DE BATALLA ---
    # El bucle principal del juego, se repite hasta que alguien gane.
    while True:
        # Se asume que 'f' es un módulo de funciones y limpia la consola para el nuevo turno.
        
        print(f"================== RONDA {turno} ==================")
        
        # 1. TURNO DEL JUGADOR HUMANO
        print(f"\n[TU TURNO] Dispara a las coordenadas del rival (Tablero de Seguimiento):")
        # Imprime el tablero del jugador que muestra sus disparos anteriores (aciertos/fallos) sobre el tablero del rival.
        jugador.tablero.imprimirTablero() 
        
        pasar_turno = False
        # Bucle interno: permite al jugador seguir disparando (ej. si acierta y el juego lo permite).
        while not pasar_turno:
            
            # Obtiene las coordenadas del disparo del usuario.
            coordenadas_disparo = jugador.obtener_disparo_humano()
            
            # Llama al método disparar: el jugador dispara a la IA, y el resultado determina si 'pasar_turno' es True o False.
            pasar_turno = jugador.disparar(ia, coordenadas_disparo)
            
            # Muestra el estado actualizado del tablero de seguimiento y del tablero propio (oculto).
            jugador.tablero.imprimirTablero()
            jugador.tablero_oculto.imprimirTablero()

        # Comprueba si el jugador humano ha ganado (todos los barcos de la IA están hundidos).
        if f.verificar_victoria(ia):
            print("\n¡VICTORIA! Todos los barcos de la IA han sido hundidos.")
            break # Sale del bucle principal (fin del juego).

        print("-" * 30)
        
        # 2. TURNO DE LA IA
        print(f"\n[TURNO DE LA IA] La IA está disparando...")

        pasar_turno = False
        # Bucle interno: permite a la IA seguir disparando.
        while not pasar_turno:
            # La IA dispara al jugador. El método 'disparar' sin coordenadas se asume que elige un tiro aleatorio o inteligente.
            pasar_turno = ia.disparar(jugador) 
        
        print("\nAsí quedó tu tablero:")
        # Muestra al jugador su propio tablero, revelando los impactos de la IA.
        jugador.tablero_oculto.imprimirTablero()
        
        # Comprueba si la IA ha ganado (todos los barcos del jugador están hundidos).
        if f.verificar_victoria(jugador):
            print("\n¡DERROTA! La IA hundió todos tus barcos.")
            break # Sale del bucle principal (fin del juego).

        # Pausa para que el jugador pueda ver el resultado del turno de la IA.
        input("\nPresiona ENTER para el siguiente turno...")
        
        # Incrementa el contador de la ronda.
        turno += 1

    print("\n================ FIN DE LA PARTIDA ===============")