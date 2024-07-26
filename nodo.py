class Nodo:
    def __init__(self, clave, detalles):
        self.clave = clave
        self.detalles = detalles
        self.izquierda = None
        self.derecha = None

class ArbolCanciones:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, detalles):
        if self.raiz is None:
            self.raiz = Nodo(clave, detalles)
        else:
            self._insertar(self.raiz, clave, detalles)

    def _insertar(self, nodo, clave, detalles):
        if clave < nodo.clave:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(clave, detalles)
            else:
                self._insertar(nodo.izquierda, clave, detalles)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(clave, detalles)
            else:
                self._insertar(nodo.derecha, clave, detalles)

    def buscar(self, clave):
        return self._buscar(self.raiz, clave)

    def _buscar(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo.detalles
        elif clave < nodo.clave:
            return self._buscar(nodo.izquierda, clave)
        else:
            return self._buscar(nodo.derecha, clave)
