#Reproduccón aleatoria
import random

class reproduccionAleatoria:
    def reproduccion_aleatoria(self):
        if self.longitud == 0:
            return
        
        indices = list(range(self.longitud))
        random.shuffle(indices)
        actual = self.cabeza
        canciones = []
        while actual:
            canciones.append(actual.cancion)
            actual = actual.siguiente
        for indice in indices:
            cancion = canciones[indice]
            print(f"Reproduciendo: {cancion.titulo} - {cancion.artista}")