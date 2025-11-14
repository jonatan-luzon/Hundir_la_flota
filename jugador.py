import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.es_ia = False
        self.tablero = None  # se asigna desde fuera

    def realizar_disparo(self, tablero_oponente):
        # jugador humano
        ...

    def ponerBarcosEnTablero(self):
        # para colocar barcos
        ...


class IA(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.es_ia = True

    def realizar_disparo(self, tablero_oponente):
        #  IA
        ...

    def ponerBarcosEnTablero(self):
        # IA barcos 
        ...
