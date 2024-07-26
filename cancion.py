class Cancion:
    def __init__(self, titulo, artista, año, duracion, popularidad):
        self.titulo = titulo
        self.artista = artista
        self.año = año
        self.duracion = duracion
        self.popularidad = popularidad

    def __repr__(self):
        return f"{self.titulo} - {self.artista}"