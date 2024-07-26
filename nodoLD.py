class NodoLD:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class DobleListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def agregar_cancion(self, cancion):
        nuevo_nodo = NodoLD(cancion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.longitud += 1

    def eliminar_cancion(self, titulo):
        actual = self.cabeza
        while actual and actual.cancion.titulo != titulo:
            actual = actual.siguiente
        if not actual:
            return False  
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        if actual == self.cabeza:
            self.cabeza = actual.siguiente
        if actual == self.cola:
            self.cola = actual.anterior
        self.longitud -= 1
        return True

    def obtener_lista(self):
        canciones = []
        actual = self.cabeza
        while actual:
            canciones.append(actual.cancion)
            actual = actual.siguiente
        return canciones
