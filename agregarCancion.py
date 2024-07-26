from nodos import Nodo

class agregarCancion:
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

    def ajustar_memoria(self):
            if self.longitud < 0:
                self.longitud = 0
                
    def __len__(self):   
        return self.longitud