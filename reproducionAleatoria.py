#Reproduccón aleatoria
    
import random

def reproduccion_aleatoria(self, seed=None):
    canciones_aleatorias = self.canciones[:] #Una lista para almacenar las canciones aleatorias
    if seed is not None:
        random.seed(seed)
    random.shuffle(canciones_aleatorias)
    return canciones_aleatorias