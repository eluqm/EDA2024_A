from cancion import Cancion
from gestor import GestorMusica

lista = GestorMusica()
lista.agregar_cancion(Cancion("Canción 1", "Artista A", 2020, 180, 85, "Alta"))
lista.agregar_cancion(Cancion("Canción 2", "Artista B", 2019, 200, 90, "Alta"))
lista.agregar_cancion(Cancion("Canción 3", "Artista C", 2021, 160, 75, "Alta"))
lista.agregar_cancion(Cancion("Canción 4", "Artista D", 2018, 190, 80, "Alta"))

print("Lista original:")
lista.imprimir_lista()

lista.cambiar_orden(1, 3)
print("\nDespués de cambiar de orden (1 a 3):")
lista.imprimir_lista()

lista.cambiar_orden(3, 0)
print("\nDespués de cambiar de orden (3 a 0):")
lista.imprimir_lista()