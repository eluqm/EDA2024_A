from cancion import Cancion

class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class Ordenamiento:
    #Ordenamiento y manipulación
    def cambiar_orden(self, posicion_actual, nueva_posicion): #Se crea el método para cambiar el órden
        if 0 <= posicion_actual < len(self.canciones) and 0 <= nueva_posicion < len(self.canciones):
            cancion = self.canciones[posicion_actual]
            del self.canciones[posicion_actual]
            self.canciones.insert(nueva_posicion, cancion)