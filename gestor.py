import cancion
import csv

class GestorMusica:
    #Lista de reproduccion
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
        
    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(f"Título: {actual.cancion.titulo}, Artista: {actual.cancion.artista}")
            actual = actual.siguiente

    def cargar_csv(self, archivo_csv):
        with open(archivo_csv, 'r') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                cancion = cancion(
                    fila['track_name'],
                    fila['artist_name'],
                    int(fila['year']),
                    int(fila['duration_ms']),
                    int(fila['popularity'])
                )
                self.agregar_cancion(cancion)