import random

class GestorMusica:
    def __init__(self):
        self.lista_canciones = []
        self.canciones_dict = {}  # Diccionario para acceso rápido

    def agregar_cancion(self, cancion):
        if cancion.titulo not in self.canciones_dict:
            self.lista_canciones.append(cancion)
            self.canciones_dict[cancion.titulo] = cancion

    def obtener_lista(self):
        return self.lista_canciones

    def eliminar_cancion(self, titulo):
        cancion = self.canciones_dict.pop(titulo, None)
        if cancion:
            self.lista_canciones.remove(cancion)

    def reproduccion_aleatoria(self):
        return random.sample(self.lista_canciones, min(len(self.lista_canciones), 5))

    def ordenar_lista(self, criterio):
        if criterio == 'popularity':
            self.lista_canciones.sort(key=lambda c: c.popularidad, reverse=True)
        elif criterio == 'year':
            self.lista_canciones.sort(key=lambda c: c.year)
        elif criterio == 'duration':
            self.lista_canciones.sort(key=lambda c: c.duracion)