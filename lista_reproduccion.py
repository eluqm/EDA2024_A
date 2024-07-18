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
    
    def ajustar_memoria(self):
        
    def __len__(self):   
        
    def mostrar_lista(self):