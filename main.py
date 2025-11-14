import funciones
from tablero import Tablero
from jugador import Jugador, IA
from funciones import ejecutar_partida
# from Clases.Tablero import Tablero
# from Clases.Jugador import Jugador
print("Iniciando juego de Hundir la Flota")

jugador = Jugador()
ia = Jugador()
jugador.ponerBarcosEnTablero()
ia.ponerBarcosEnTablero()
