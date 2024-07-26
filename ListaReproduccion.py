from nodos import Nodo

class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

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
    
    def cambiar_orden(self, posicion_actual, nueva_posicion):
        if posicion_actual < 0 or posicion_actual >= self.longitud or \
           nueva_posicion < 0 or nueva_posicion >= self.longitud or \
           posicion_actual == nueva_posicion:
            return

        nodo_actual = self.obtener_nodo(posicion_actual)
        if not nodo_actual:
            return

        #Remueve el nodo de su posición actual
        if nodo_actual.anterior:
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
        else:
            self.cabeza = nodo_actual.siguiente

        if nodo_actual.siguiente:
            nodo_actual.siguiente.anterior = nodo_actual.anterior
        else:
            self.cola = nodo_actual.anterior

        #Inserta el nodo en la nueva posición, cambiando el orden
        if nueva_posicion == 0:
            nodo_actual.anterior = None
            nodo_actual.siguiente = self.cabeza
            self.cabeza.anterior = nodo_actual
            self.cabeza = nodo_actual
        elif nueva_posicion == self.longitud - 1:
            nodo_actual.siguiente = None
            nodo_actual.anterior = self.cola
            self.cola.siguiente = nodo_actual
            self.cola = nodo_actual
        else:
            nodo_destino = self.obtener_nodo(nueva_posicion)
            nodo_actual.anterior = nodo_destino.anterior
            nodo_actual.siguiente = nodo_destino
            nodo_destino.anterior.siguiente = nodo_actual
            nodo_destino.anterior = nodo_actual

    def obtener_nodo(self, indice): #Obtiene el nodo 
        if indice < 0 or indice >= self.longitud:
            return None
        if indice < self.longitud // 2:
            actual = self.cabeza
            for _ in range(indice):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self.longitud - 1, indice, -1):
                actual = actual.anterior
        return actual
    
    def ajustar_memoria(self):
        if self.longitud < 0:
            self.longitud = 0

    def __len__(self):   
        return self.longitud