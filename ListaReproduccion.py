from Nodos import Nodo
from ArbolRN import ArbolRojoNegro
from DobleLE import DobleListaEnlazada
import random
import heapq

class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    #Agregar una nueva canción, mediante el uso de List
    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.longitud += 1
        self.ajustar_memoria()

    #Eliminar una nueva canción, mediante el uso de List
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
        self.longitud -= 1
        self.ajustar_memoria()
        return True
    
    #Método para manejar una reproducción aleatoria
    def reproduccion_aleatoria(self):
        if self.longitud == 0:
            return
        
        heap_canciones = []
        actual = self.cabeza
        while actual:
            # Usar un número aleatorio como prioridad
            prioridad = random.random()
            heapq.heappush(heap_canciones, (prioridad, actual.cancion))
            actual = actual.siguiente
        
        while heap_canciones:
            _, cancion = heapq.heappop(heap_canciones)
            print(f"Reproduciendo: {cancion.titulo} - {cancion.artista}")
    
    #Método para cambiar orden
    def cambiar_orden(self, posicion_actual, nueva_posicion):
        DobleListaEnlazada.cambiar_orden(self, posicion_actual, nueva_posicion)
    
    #Método para cambiar orden por criterio
    def ordenar_por_criterio(self, criterio):
        """
        Este método reordena la lista de reproducción según el criterio especificado
        utilizando un Árbol Rojo-Negro.
        
        Args:
            criterio (str): El criterio de ordenación ('titulo', 'artista', 'año', etc.)
        """
        arbol = ArbolRojoNegro(criterio)
        
        # Inserta todas las canciones en el árbol
        actual = self.cabeza
        while actual:
            arbol.insertar(actual.cancion)
            actual = actual.siguiente
        
        # Reconstruye la lista ordenada
        self.cabeza = None
        self.cola = None
        self.longitud = 0
        
        def recorrer_arbol(nodo):
            if nodo:
                recorrer_arbol(nodo.izquierda)
                self.agregar_cancion(nodo.cancion)
                recorrer_arbol(nodo.derecha)
        
        recorrer_arbol(arbol.raiz)