class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.grid = [[' ']*tamaño for _ in range(tamaño)]
        self.barcos_restantes = 0

    def colocar_barco(self, fila, columna, tamaño, orientacion):
        ...
    
    def recibir_disparo(self, fila, columna):
        ...
