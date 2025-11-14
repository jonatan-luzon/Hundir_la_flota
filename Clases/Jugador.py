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