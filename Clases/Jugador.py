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
                self.tablero_oculto.imprimirTablero()
                print("Poniendo barco de eslora:", int(barco))
                self.tablero_oculto.ponerBarco(int(barco))

    def ponerBarco(self, eslora = 4, num_intentos = 100):
        num_max_filas = ALTURA_TABLERO - 1
        num_max_columnas = BASE_TABLERO - 1
        contador = 0
        while contador < num_intentos:
            barco = []
            pieza_original = (random.randint(0, num_max_filas), random.randint(0, num_max_columnas))
            barco.append(pieza_original)

            orientacion = random.choice(["N","S","O","E"])
            print("Orientación elegida:", orientacion)
            fila = pieza_original[0]
            columna = pieza_original[1]

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
                barco.append(pieza_nueva)
            
            print("Barco generado:", barco)
            tablero_temp = self.insertar_barcos_en_tablero_plus(barco)

            if type(tablero_temp) == np.ndarray:
                return tablero_temp

            contador += 1

        print("Tengo que intentar colocar otro barco")

    def insertar_barcos_en_tablero_plus(self, barcos, simbolo_barco = "O"):
        tablero_temp = self.tablero_oculto.tablero.copy()
        num_max_filas = ALTURA_TABLERO
        num_max_columnas = BASE_TABLERO

        for pieza in barcos:
            fila = pieza[0]
            columna = pieza[1]
            if fila >= 0 and fila < num_max_filas and columna >= 0 and columna < num_max_columnas:
                tablero_temp[fila, columna] = simbolo_barco
        
        return tablero_temp

    def disparar(rival, disparo):
        disparo = (random.randint(0, BASE_TABLERO), random.randint(0, ALTURA_TABLERO))
        match rival.tablero[disparo]:
            case "O":
                rival.tablero[disparo] = "X"
                rival.tablero_oculto[disparo] = "X"
                print("Tocado")
            case "~":
                rival.tablero[disparo] = "-"
                rival.tablero_oculto[disparo] = "~"
                print("Agua")
            case "X", "-":
                print("Ya has disparado aquí")

    

    #def comprobarDerrota():