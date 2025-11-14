import random

def ponerBarcosEnTablero(self):
    print(f"\n{self.nombre}, coloca tus barcos:")

    # Puedes ajustar esta lista como prefieras
    tamanos_barcos = [4, 3, 3, 2, 2, 1, 1]

    for tam in tamanos_barcos:
        colocado = False

        while not colocado:
            print(f"\nBarco de tamaño {tam}")

            try:
                fila = int(input("Fila: "))
                col = int(input("Columna: "))
                orient = input("Orientación (H/V): ").upper()

                if orient not in ("H", "V"):
                    print("Debes escribir H o V.")
                    continue

                exito = self.tablero.colocar_barco(fila, col, tam, orient)

                if exito:
                    print("Barco colocado correctamente.")
                    colocado = True
                else:
                    print("No se puede colocar el barco ahí. Intenta otra posición.")

            except ValueError:
                print("Introduce números válidos.")

# Para la IA
def ponerBarcosEnTableroIA(self):
    tamanos_barcos = [4, 3, 3, 2, 2, 1, 1]

    for tam in tamanos_barcos:
        colocado = False

        while not colocado:
            fila = random.randint(0, self.TAMAÑO_TABLERO - 1)
            col = random.randint(0, self.TAMAÑO_TABLERO - 1)
            orient = random.choice(["H", "V"])

            exito = self.tablero.colocar_barco(fila, col, tam, orient)

            if exito:
                colocado = True

    print(f"{self.nombre} ha colocado sus barcos.")


# Control del flujo del juego (alternancia de turnos)
def ejecutar_partida(jugador, computadora):
    numero_turno = 1

    while jugador.tablero.barcos_restantes > 0 and computadora.tablero.barcos_restantes > 0:

        # Turno del jugador humano
        print(f"\n=== RONDA {numero_turno} ===")
        print(f"Turno de {jugador.nombre}:")

        jugador.realizar_disparo(computadora.tablero)

        if computadora.tablero.barcos_restantes == 0:
            print(f"\n¡Victoria para {jugador.nombre}! Todos los barcos enemigos han sido hundidos.")
            return

        # Turno de la IA
        print(f"\nTurno de {computadora.nombre} (IA):")

        computadora.realizar_disparo(jugador.tablero)

        if jugador.tablero.barcos_restantes == 0:
            print("\nLa IA ha ganado la partida. Mejor suerte la próxima vez.")
            return

        numero_turno += 1

    print("\nPartida finalizada.")


# Lógica de disparo
def realizar_disparo(self, tablero_enemigo):

    # Comportamiento de la IA
    if self.es_ia:
        while True:
            fila_aleatoria = random.randint(0, self.TAMAÑO_TABLERO - 1)
            columna_aleatoria = random.randint(0, self.TAMAÑO_TABLERO - 1)

            resultado_tiro = tablero_enemigo.recibir_disparo(fila_aleatoria, columna_aleatoria)

            # Solo informamos si no ha repetido casilla
            if resultado_tiro != 'YaDisparado':
                print(f"La IA dispara a la casilla ({fila_aleatoria}, {columna_aleatoria}) → {resultado_tiro}")
                break

    else:
        # Aquí va la lógica del disparo del jugador humano (input, validación, etc.)
        pass
