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
       
    def ajustar_memoria(self):
        
    def __len__(self):   
        
    def mostrar_lista(self):