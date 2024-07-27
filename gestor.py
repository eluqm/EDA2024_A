import random
import heapq
from nodoLD import DobleListaEnlazada
from ArbolRN import ArbolRojoNegro
class GestorMusica:
    def __init__(self):
        self.lista_canciones = DobleListaEnlazada()
        self.canciones_dict = {}  # Diccionario para acceso rápido

    def agregar_cancion(self, cancion):
        if cancion.titulo not in self.canciones_dict:
            self.lista_canciones.agregar_cancion(cancion)
            self.canciones_dict[cancion.titulo] = cancion

    def obtener_lista(self):
        return self.lista_canciones.obtener_lista()

    def eliminar_cancion(self, titulo):
        if self.lista_canciones.eliminar_cancion(titulo):
            del self.canciones_dict[titulo]

    def reproduccion_aleatoria(self):
        canciones = self.obtener_lista()
        heap_canciones = []
        for cancion in canciones:
            prioridad = random.random()
            heapq.heappush(heap_canciones, (prioridad, cancion))
        seleccion = []
        while heap_canciones and len(seleccion) < 5:
            _, cancion = heapq.heappop(heap_canciones)
            seleccion.append(cancion)
        return seleccion

    def ordenar_lista(self, criterio):
        canciones = self.obtener_lista()
        if criterio == 'popularity':
            canciones.sort(key=lambda c: c.popularidad, reverse=True)
        elif criterio == 'año':
            canciones.sort(key=lambda c: c.año)
        elif criterio == 'duration':
            canciones.sort(key=lambda c: c.duracion)
        # Reconstruir la lista doblemente enlazada ordenada
        nueva_lista = DobleListaEnlazada()
        for cancion in canciones:
            nueva_lista.agregar_cancion(cancion)  # Cambiado de append a agregar_cancion
        self.lista_canciones = nueva_lista  # Reemplazar la lista con la nueva lista ordenada

    def cambiar_orden(self, cancion_titulo, nueva_popularidad):
        # Encuentra la canción y cambia su popularidad
        if cancion_titulo in self.canciones_dict:
            cancion = self.canciones_dict[cancion_titulo]
            cancion.popularidad = nueva_popularidad

            # Reconstruir el árbol rojo-negro con la nueva popularidad
            self.arbol = ArbolRojoNegro('popularidad')
            for cancion in self.canciones_dict.values():
                self.arbol.insertar(cancion)

            # Reconstruir la lista doblemente enlazada ordenada por popularidad
            canciones = sorted(self.canciones_dict.values(), key=lambda c: c.popularidad, reverse=True)
            self.lista_canciones = DobleListaEnlazada()
            for cancion in canciones:
                self.lista_canciones.agregar_cancion(cancion)
        else:
            print(f"Canción con título '{cancion_titulo}' no encontrada.")