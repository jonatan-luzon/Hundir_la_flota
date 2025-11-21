import numpy as np
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_victoria(jugador_rival):
    # Cuenta los barcos (O) que quedan en el tablero oculto del rival
    return np.count_nonzero(jugador_rival.tablero_oculto.tablero == "O") == 0

