class eliminarCancion:
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
    
    def ajustar_memoria(self):
            if self.longitud < 0:
                self.longitud = 0
                
    def __len__(self):   
        return self.longitud