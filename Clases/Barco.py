class Barco:
    def __init__(self, coordenadas):

        self.coordenadas = set(coordenadas)
        self.impactos = set()

    def recibir_disparo(self, fila, col):

        if (fila, col) not in self.coordenadas:
            return None

        self.impactos.add((fila, col))

        if self.esta_hundido():
            return "Hundido"
        return "Tocado"

    def esta_hundido(self):
        return self.impactos == self.coordenadas

    def vidas(self):
        return len(self.coordenadas) - len(self.impactos)
