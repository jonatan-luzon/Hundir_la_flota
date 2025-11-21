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
    
def obtener_disparo_humano(self):
        # Inicia un bucle infinito para seguir pidiendo coordenadas hasta que sean válidas.
        while True:
            try:
                # Pide la Fila al usuario. Se resta 1 porque los humanos cuentan desde 1
                fila = int(input(f"Fila ({1}-{ALTURA_TABLERO}): ")) - 1
                
                # Pide la Columna al usuario. También se resta 1 por la indexación base 0.
                columna = int(input(f"Columna ({1}-{BASE_TABLERO}): ")) - 1
                
                # Verifica que las coordenadas (ya ajustadas a base 0) estén dentro de los límites del tablero.
                if 0 <= fila < ALTURA_TABLERO and 0 <= columna < BASE_TABLERO:
                    # Si son válidas, se sale del bucle y devuelve la tupla (fila, columna).
                    return (fila, columna)
                else:
                    # Mensaje de error si las coordenadas están fuera de los límites definidos.
                    print("Coordenadas fuera de rango. Inténtalo de nuevo.")
            
            # Captura un error si el usuario introduce texto o cualquier cosa que no sea un número entero.
            except ValueError:
                print("Entrada inválida. Introduce solo números.")