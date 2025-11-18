import numpy as np
import random
from variables import *

class Tablero:

    def __init__(self):
        self.tablero = np.full((BASE_TABLERO, ALTURA_TABLERO), " ")

    def ponerBarco(self, eslora = 4, num_intentos = 100):
        num_max_filas = ALTURA_TABLERO - 1
        num_max_columnas = BASE_TABLERO - 1
        contador = 0
        barco_colocado = False
        while contador < num_intentos and not barco_colocado:
            barco = []
            pieza_original = (random.randint(0, num_max_filas), random.randint(0, num_max_columnas))
            comprovacion = self.compararSolapamientoBarcos(pieza_original)
            barco.append(pieza_original)

            orientacion = random.choice(["N","S","O","E"])
            fila = pieza_original[0]
            columna = pieza_original[1]
            comprovacion = True
            for i in range(eslora - 1):
                match orientacion:
                    case "N":
                        fila -= 1
                    case "S":
                        fila += 1
                    case "O":
                        columna -= 1
                    case "E":
                        columna += 1
                pieza_nueva = (fila, columna)
                comprovacion = comprovacion if self.compararLimiteTablero(pieza_nueva) else False
                if comprovacion:
                    comprovacion = comprovacion if self.compararSolapamientoBarcos(pieza_nueva) else False
                barco.append(pieza_nueva)

            tablero_temp = None
            if comprovacion:
                tablero_temp = self.insertar_barcos_en_tablero_plus(barco)
            else: 
                print("No se puede colocar el barco aquí.")

            if type(tablero_temp) == np.ndarray:
                barco_colocado = True
                self.tablero = tablero_temp
                break

            contador += 1

    def insertar_barcos_en_tablero_plus(self, barcos, simbolo_barco = "O"):
        tablero_temp = self.tablero.copy()
        num_max_filas = ALTURA_TABLERO
        num_max_columnas = BASE_TABLERO

        for pieza in barcos:
            fila = pieza[0]
            columna = pieza[1]
            tablero_temp[fila, columna] = simbolo_barco
        return tablero_temp
    
    def compararLimiteTablero(self, pieza):
        fila = pieza[0]
        columna = pieza[1]
        # evitar que la pieza se salga fuera del tablero
        if fila < 0 or fila >= ALTURA_TABLERO or columna < 0 or columna >= BASE_TABLERO:
            return False
        return True
        
    def compararSolapamientoBarcos(self, pieza, simbolo_barco="O"):
        fila = pieza[0]
        columna = pieza[1]
        for despl_fila in [-1, 0, 1]:
            for despl_columna in [-1, 0, 1]:
                nueva_fila = fila + despl_fila
                nueva_columna = columna + despl_columna
                # verificar que la casilla vecina existe
                if 0 <= nueva_fila < ALTURA_TABLERO and 0 <= nueva_columna < BASE_TABLERO:
                    if self.tablero[nueva_fila, nueva_columna] == simbolo_barco:
                        return False
        return True

    def imprimirTablero(self):
        print(self.tablero)