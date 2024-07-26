class cambiarOrden:
    #Cambiar orden
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