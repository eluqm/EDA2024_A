class Nodo:
    def __init__(self, clave, detalles):
        self.clave = clave
        self.detalles = detalles
        self.izquierda = None
        self.derecha = None

class NodoRN:
    def __init__(self, cancion, color="rojo"):
        self.cancion = cancion
        self.color = color
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolCanciones:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, detalles):
        if self.raiz is None:
            self.raiz = Nodo(clave, detalles)
        else:
            self.raiz = self._insertar(self.raiz, clave, detalles)

    def _insertar(self, nodo, clave, detalles):
        if nodo is None:
            return Nodo(clave, detalles)
        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, detalles)
        else:
            nodo.derecha = self._insertar(nodo.derecha, clave, detalles)

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        return self._balancear(nodo)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _balancear(self, nodo):
        balance = self._factor_balance(nodo)
        if balance > 1:
            if self._factor_balance(nodo.izquierda) < 0:
                nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)
        if balance < -1:
            if self._factor_balance(nodo.derecha) > 0:
                nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)
        return nodo

    def _factor_balance(self, nodo):
        if nodo is None:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def _rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        x.altura = 1 + max(self._altura(x.izquierda), self._altura(x.derecha))
        return x
    
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
