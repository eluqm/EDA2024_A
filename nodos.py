#la clase Nodo, se usa para una lista doblemente enlazada

class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

#Nodo para arbol BST
class NodoRN:
    def __init__(self, cancion, color="rojo"):
        self.cancion = cancion
        self.color = color  # "rojo" o "negro"
        self.izquierda = None
        self.derecha = None
        self.padre = None