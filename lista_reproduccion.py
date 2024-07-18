from cancion import Cancion
from nodo import Nodo

class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0
        
    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamaño += 1
        self.ajustar_memoria()
        
    def eliminar_cancion(self, titulo):
        actual = self.cabeza
        while actual and actual.cancion.titulo != titulo:
            actual = actual.siguiente
        if not actual:
            return False  # La canción no se encontró
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        if actual == self.cabeza:
            self.cabeza = actual.siguiente
        if actual == self.cola:
            self.cola = actual.anterior
        self.tamaño -= 1
        self.ajustar_memoria()
        return True
    
    #Ordenamiento y manipulación
    def cambiar_orden(self, posicion_actual, nueva_posicion): #Se crea el método para cambiar el órden
        if 0 <= posicion_actual < len(self.canciones) and 0 <= nueva_posicion < len(self.canciones):
            cancion = self.canciones[posicion_actual]
            del self.canciones[posicion_actual]
            self.canciones.insert(nueva_posicion, cancion)
    
    def ajustar_memoria(self):
        if self.tamaño < 0:
            self.tamaño = 0
            
    def __len__(self):   
         return self.tamaño
     
    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(f"Título: {actual.cancion.titulo}, Artista: {actual.cancion.artista}")
            actual = actual.siguiente