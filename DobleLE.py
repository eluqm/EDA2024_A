class DobleListaEnlazada:
    def cambiar_orden(self, lista, posicion_actual, nueva_posicion):
        if posicion_actual < 0 or posicion_actual >= lista.longitud or \
           nueva_posicion < 0 or nueva_posicion >= lista.longitud or \
           posicion_actual == nueva_posicion:
            return

        nodo_actual = self.obtener_nodo(lista, posicion_actual)
        if not nodo_actual:
            return

        # Remueve el nodo de su posición actual
        if nodo_actual.anterior:
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
        else:
            lista.cabeza = nodo_actual.siguiente

        if nodo_actual.siguiente:
            nodo_actual.siguiente.anterior = nodo_actual.anterior
        else:
            lista.cola = nodo_actual.anterior

        # Inserta el nodo en la nueva posición, cambiando el orden
        if nueva_posicion == 0:
            nodo_actual.anterior = None
            nodo_actual.siguiente = lista.cabeza
            lista.cabeza.anterior = nodo_actual
            lista.cabeza = nodo_actual
        elif nueva_posicion == lista.longitud - 1:
            nodo_actual.siguiente = None
            nodo_actual.anterior = lista.cola
            lista.cola.siguiente = nodo_actual
            lista.cola = nodo_actual
        else:
            nodo_destino = self.obtener_nodo(lista, nueva_posicion)
            nodo_actual.anterior = nodo_destino.anterior
            nodo_actual.siguiente = nodo_destino
            nodo_destino.anterior.siguiente = nodo_actual
            nodo_destino.anterior = nodo_actual

    def obtener_nodo(self, lista, indice):
        if indice < 0 or indice >= lista.longitud:
            return None
        if indice <= lista.longitud // 2:
            actual = lista.cabeza
            for _ in range(indice):
                actual = actual.siguiente
        else:
            actual = lista.cola
            for _ in range(lista.longitud - 1, indice, -1):
                actual = actual.anterior
        return actual

    def ajustar_memoria(self, lista):
        if lista.longitud < 0:
            lista.longitud = 0