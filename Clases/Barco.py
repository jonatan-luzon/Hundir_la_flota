class Barco:
    def __init__(self, coordenadas):
        # self.coordenadas: Conjunto de tuplas (fila, col) que definen la posición del barco (su vida total).
        self.coordenadas = set(coordenadas)
        # self.impactos: Conjunto de tuplas (fila, col) que han sido alcanzadas.
        self.impactos = set()

    def recibir_disparo(self, fila, col):
        # Verifica si el disparo falló (no está en las coordenadas del barco).
        if (fila, col) not in self.coordenadas:
            return None # Retorna None si es 'agua' (fallo).

        # Si acierta, añade la coordenada al registro de impactos.
        self.impactos.add((fila, col))

        # Comprueba si el barco se ha hundido con este disparo.
        if self.esta_hundido():
            return "Hundido"
        # Si no se hundió, solo fue un 'Tocado'.
        return "Tocado"

    def esta_hundido(self):
        # Devuelve True si todas las coordenadas han sido impactadas.
        # Es decir, si el conjunto de impactos es igual al conjunto de coordenadas.
        return self.impactos == self.coordenadas

    def vidas(self):
        # Calcula la vida restante: tamaño total - número de impactos.
        return len(self.coordenadas) - len(self.impactos)
