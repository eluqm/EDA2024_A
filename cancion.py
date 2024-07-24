class Cancion:
    def __init__(self, titulo, artista, album, año, duracion, popularidad):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.año = año
        self.duracion = duracion
        self.popularidad = popularidad

    def __str__(self):
        return f"{self.titulo} - {self.artista} - {self.album} - {self.duracion}"