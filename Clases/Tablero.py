import numpy as np
import random
from variables import *

class Tablero:

    def __init__(self):
        self.tablero = np.full((BASE_TABLERO, ALTURA_TABLERO), "~")
        
    def ponerBarco(self, eslora = 4, num_intentos = 100):
        num_max_filas = ALTURA_TABLERO - 1
        num_max_columnas = BASE_TABLERO - 1
        contador = 0
        barco_colocado = False
        while contador < num_intentos and not barco_colocado:
            barco = []
            #pieza_original = (random.randint(0, num_max_filas), random.randint(0, num_max_columnas))
            pieza_original = (5,3)
            barco.append(pieza_original)

            #orientacion = random.choice(["N","S","O","E"])
            orientacion = "N"
            print("Orientación elegida:", orientacion)
            fila = pieza_original[0]
            columna = pieza_original[1]

            for i in range(eslora - 1):
                match orientacion:
                    case "N":
                        fila -= 1
                        #compararLimiteTablero()
                        #compararSolapamientoBarcos()
                    case "S":
                        fila += 1
                    case "O":
                        columna -= 1
                    case "E":
                        columna += 1
                pieza_nueva = (fila, columna)
                barco.append(pieza_nueva)
            
            
            #compararLimiteTablero()
            #compararSolapamientoBarcos()

            tablero_temp = self.insertar_barcos_en_tablero_plus(barco)

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
            if fila >= 0 and fila < num_max_filas and columna >= 0 and columna < num_max_columnas:
                tablero_temp[fila, columna] = simbolo_barco
        
        return tablero_temp
    
    def imprimirTablero(self):
        print(self.tablero)