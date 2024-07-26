from Nodos import NodoRN

class ArbolRojoNegro:
    def __init__(self, criterio):
        self.raiz = None
        self.criterio = criterio

    def _rotar_izquierda(self, nodo):
        derecho = nodo.derecha
        nodo.derecha = derecho.izquierda
        if derecho.izquierda is not None:
            derecho.izquierda.padre = nodo
        derecho.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = derecho
        elif nodo == nodo.padre.izquierda:
            nodo.padre.izquierda = derecho
        else:
            nodo.padre.derecha = derecho
        derecho.izquierda = nodo
        nodo.padre = derecho

    def _rotar_derecha(self, nodo):
        izquierdo = nodo.izquierda
        nodo.izquierda = izquierdo.derecha
        if izquierdo.derecha is not None:
            izquierdo.derecha.padre = nodo
        izquierdo.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = izquierdo
        elif nodo == nodo.padre.derecha:
            nodo.padre.derecha = izquierdo
        else:
            nodo.padre.izquierda = izquierdo
        izquierdo.derecha = nodo
        nodo.padre = izquierdo

    def _ajustar_insercion(self, nodo):
        while nodo != self.raiz and nodo.padre.color == "rojo":
            if nodo.padre == nodo.padre.padre.izquierda:
                tio = nodo.padre.padre.derecha
                if tio and tio.color == "rojo":
                    nodo.padre.color = "negro"
                    tio.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.derecha:
                        nodo = nodo.padre
                        self._rotar_izquierda(nodo)
                    nodo.padre.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    self._rotar_derecha(nodo.padre.padre)
            else:
                tio = nodo.padre.padre.izquierda
                if tio and tio.color == "rojo":
                    nodo.padre.color = "negro"
                    tio.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izquierda:
                        nodo = nodo.padre
                        self._rotar_derecha(nodo)
                    nodo.padre.color = "negro"
                    nodo.padre.padre.color = "rojo"
                    self._rotar_izquierda(nodo.padre.padre)
        self.raiz.color = "negro"

    def _insertar(self, nodo, cancion):
        if nodo is None:
            return NodoRN(cancion, "rojo")

        valor_nodo = getattr(nodo.cancion, self.criterio)
        valor_cancion = getattr(cancion, self.criterio)

        if valor_cancion < valor_nodo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoRN(cancion, "rojo")
                nodo.izquierda.padre = nodo
                self._ajustar_insercion(nodo.izquierda)
            else:
                self._insertar(nodo.izquierda, cancion)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoRN(cancion, "rojo")
                nodo.derecha.padre = nodo
                self._ajustar_insercion(nodo.derecha)
            else:
                self._insertar(nodo.derecha, cancion)

        return nodo

    def insertar(self, cancion):
        if self.raiz is None:
            self.raiz = NodoRN(cancion, "negro")
        else:
            self._insertar(self.raiz, cancion)

    def _mostrar_en_orden(self, nodo):
        if nodo is not None:
            self._mostrar_en_orden(nodo.izquierda)
            print(nodo.cancion)
            self._mostrar_en_orden(nodo.derecha)

    def mostrar_en_orden(self):
        self._mostrar_en_orden(self.raiz)