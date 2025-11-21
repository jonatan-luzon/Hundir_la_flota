import numpy as np
from Clases.Tablero import Tablero
import random
from variables import *

class Jugador:

    def __init__(self):

        self.tablero = Tablero()
        self.tablero_oculto = Tablero()
        self.barcos = {"1":4, "2":3, "3":2, "4":1}  # eslora: cantidad

    def ponerBarcosEnTablero(self):
        for barco in reversed(self.barcos):
            for cantidad in range(self.barcos[barco]):
                print("Poniendo barco de eslora:", int(barco))
                self.tablero_oculto.ponerBarco(int(barco))

    def disparar(self, rival, disparo = None):
        
        # Generar disparo aleatorio solo si no se pasó uno (Turno de la IA)
        if disparo is None:
            # RANGO CORRECTO: Base/Altura - 1 para evitar IndexError
            disparo = (random.randint(0, BASE_TABLERO - 1), random.randint(0, ALTURA_TABLERO - 1))

        # 1. Obtenemos el valor de la celda del tablero REAL del rival
        valor_celda = rival.tablero_oculto.tablero[disparo]
        
        # 2. Comprobamos el resultado y actualizamos ambos tableros
        match valor_celda:
            case "O":
                self.tablero.tablero[disparo] = "X"
                rival.tablero_oculto.tablero[disparo] = "X"
                print("¡TOCADO!")
            case " ": 
                # Agua: Si estaba vacío (" "), se marca con "~" en ambos tableros
                self.tablero.tablero[disparo] = "~"
                rival.tablero_oculto.tablero[disparo] = "~"
                print("¡AGUA!")
                return True
            case "X" | "~": 
                # Ya disparado: Si ya era "X" (tocado) o "~" (agua)
                print("Ya has disparado aquí. No pasa nada.")
            case _:
                print("¡Error de estado desconocido!")
        
        return False
    
    def obtener_disparo_humano():
        while True:
            try:
                fila = int(input(f"Fila ({1}-{ALTURA_TABLERO}): ")) - 1
                columna = int(input(f"Columna ({1}-{BASE_TABLERO}): ")) - 1
                
                if 0 <= fila < ALTURA_TABLERO and 0 <= columna < BASE_TABLERO:
                    return (fila, columna)
                else:
                    print("Coordenadas fuera de rango. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Introduce solo números.")