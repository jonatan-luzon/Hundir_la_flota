import numpy as np
import random
from variables import *

class Tablero:

    def __init__(self):
        # Inicializa un array lleno de espacios en blanco
        self.tablero = np.full((BASE_TABLERO, ALTURA_TABLERO), " ")

    def ponerBarco(self, eslora):
        """
        Algoritmo robusto para colocar un barco aleatorio (modifica self.tablero directamente).
        """
        max_filas = ALTURA_TABLERO - 1
        max_cols = BASE_TABLERO - 1

        for _ in range(NUM_INTENTOS):
            
            # 1. Elegir Origen y Orientación Aleatoria
            fila_origen = random.randint(0, max_filas)
            col_origen = random.randint(0, max_cols)
            orientacion = random.choice(["N", "S", "E", "O"])

            coordenadas_barco = []
            fila_actual = fila_origen
            col_actual = col_origen
            es_posible = True
            
            # 2. Bucle de Cálculo y Validación de Todas las Piezas
            for i in range(eslora):
                coord = (fila_actual, col_actual)

                # Validar 1: ¿Se sale del mapa?
                if not self.compararLimiteTablero(coord):
                    es_posible = False
                    break 
                
                # Validar 2: ¿Choca con otro barco o sus vecinos?
                if not self.compararSolapamientoBarcos(coord):
                    es_posible = False
                    break

                coordenadas_barco.append(coord)

                if orientacion == "N": fila_actual -= 1
                elif orientacion == "S": fila_actual += 1
                elif orientacion == "E": col_actual += 1
                elif orientacion == "O": col_actual -= 1

            if es_posible:
                #  LLAMADA A LA FUNCIÓN DE INSERCIÓN DIRECTA
                self.insertar_barcos_en_tablero(coordenadas_barco) 
                return True # Éxito: el barco fue colocado

        # Si se agotan los intentos, devuelve False (lo cual es raro con 100 intentos)
        return False 

    def insertar_barcos_en_tablero(self, coordenadas, simbolo="O"):
        for f, c in coordenadas:
            self.tablero[f, c] = simbolo
            
    
    def compararLimiteTablero(self, pieza):
        fila = pieza[0]
        columna = pieza[1]
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
                if 0 <= nueva_fila < ALTURA_TABLERO and 0 <= nueva_columna < BASE_TABLERO:
                    # Comprueba si en la casilla vecina ya hay un barco
                    if self.tablero[nueva_fila, nueva_columna] == simbolo_barco:
                        return False
        return True

    def imprimirTablero(self):
        print(self.tablero)

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
