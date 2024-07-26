import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, QListWidget, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from VentanaPlaylist import VentanaPlaylist
from cancion import Cancion
from gestor import GestorMusica 
from nodo import ArbolCanciones
import csv

# Crear una instancia del árbol
arbol = ArbolCanciones()

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.gestor = GestorMusica()
        self.arbol = ArbolCanciones()  # Definir el árbol aquí
        self.cargar_datos()  # Cargar los datos en el árbol
        self.initUI()
        self.playlist = []

    def cargar_datos(self):
        with open('spotify_data.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                clave = (row['artist_name'], row['track_name'])
                detalles = {
                    'year': int(row['year']),
                    'duration_ms': int(row['duration_ms']),
                    'genre': row['genre'],
                    'popularity': int(row.get('popularity', 0))  
                }
                self.arbol.insertar(clave, detalles) 

    def initUI(self):
        # Crear los elementos de la interfaz
        self.header = QWidget(self)
        self.searchArtistInput = QLineEdit(self)
        self.searchArtistInput.setPlaceholderText('Buscar por nombre de artista...')
        self.searchTrackInput = QLineEdit(self)
        self.searchTrackInput.setPlaceholderText('Buscar por nombre de canción...')
        self.yearFilterInput = QComboBox(self)
        self.yearFilterInput.addItem('Todos los años')

        # Cargar años en el comboBox
        years = sorted(set(nodo.detalles['year'] for nodo in self._iterar_nodos(self.arbol.raiz)))
        self.yearFilterInput.addItems(map(str, years))

        self.searchButton = QPushButton('Buscar', self)
        self.resultList = QListWidget(self)
        self.playlistButton = QPushButton('Playlist', self)
        self.addToPlaylistButton = QPushButton('Añadir a Playlist', self)

        # Encabezado
        self.headerLayout = QHBoxLayout()
        self.userImage = QLabel(self)
        self.userImage.setPixmap(QPixmap('img/usericon.png').scaled(50, 50))
        self.userName = QLabel('Estructura de datos y algoritmos', self)
        self.headerLayout.addWidget(self.userImage)
        self.headerLayout.addWidget(self.userName)
        self.header.setLayout(self.headerLayout)

        # Layout principal
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.header)  # Encabezado en la parte superior
        self.mainLayout.addWidget(QLabel('Búsqueda de Canciones'))
        self.mainLayout.addWidget(self.searchArtistInput)
        self.mainLayout.addWidget(self.searchTrackInput)
        self.mainLayout.addWidget(QLabel('Filtrar por Año'))
        self.mainLayout.addWidget(self.yearFilterInput)
        self.mainLayout.addWidget(self.searchButton)
        self.mainLayout.addWidget(self.resultList)
        self.mainLayout.addWidget(self.addToPlaylistButton)  # Botón Añadir a Playlist en la parte inferior
        self.mainLayout.addWidget(self.playlistButton)  # Botón Playlist en la parte inferior

        self.setLayout(self.mainLayout)
        self.setWindowTitle('Music Search App')
        self.setGeometry(100, 100, 800, 600)

        # Conectar los botones
        self.searchButton.clicked.connect(self.searchSongs)
        self.addToPlaylistButton.clicked.connect(self.addToPlaylist)
        self.playlistButton.clicked.connect(self.showPlaylist)

        # Aplicar estilos
        self.applyStyles()

    def _iterar_nodos(self, nodo):
        """ Generador para iterar sobre todos los nodos en el árbol. """
        if nodo:
            yield nodo
            yield from self._iterar_nodos(nodo.izquierda)
            yield from self._iterar_nodos(nodo.derecha)


    def applyStyles(self):
        # Hoja de estilo
        styleSheet = """
        QWidget {
            background-color: #f0f0f0;
        }
        QLabel {
            color: #333;
            font-size: 14px;
        }
        QLineEdit {
            padding: 5px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        QComboBox {
            padding: 5px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        QPushButton {
            padding: 10px;
            font-size: 14px;
            background-color: #16378a;
            color: white;
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #14327d;
        }
        QListWidget {
            padding: 10px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: white;
        }
        QListWidget::item {
            padding: 5px;
            border-bottom: 1px solid #eee;
        }
        QListWidget::item:selected {
            background-color: #0a1226;
        }
        QPushButton#playlistButton {
            background-color: #16378a;
            color: white;
            font-weight: bold;
        }
        QPushButton#playlistButton:hover {
            background-color: #14327d;
        }
        QPushButton#addToPlaylistButton {
            background-color: #28a745;
            color: white;
            font-weight: bold;
        }
        QPushButton#addToPlaylistButton:hover {
            background-color: #218838;
        }
        """
        self.setStyleSheet(styleSheet)

    def searchSongs(self):
        artist = self.searchArtistInput.text().lower()
        track = self.searchTrackInput.text().lower()
        year = self.yearFilterInput.currentText()

        # Preparar lista de resultados
        results = []

        def buscar_canciones(nodo):
            if nodo:
                # Comprobar si el nodo actual cumple con los criterios de búsqueda
                if artist in nodo.clave[0].lower() and track in nodo.clave[1].lower():
                    if year == 'Todos los años' or year == str(nodo.detalles['year']):
                        results.append((nodo.clave[1], nodo.clave[0], nodo.detalles['genre'], nodo.detalles['year'], nodo.detalles['duration_ms'], nodo.detalles['popularity']))
                # Buscar en subárboles
                buscar_canciones(nodo.izquierda)
                buscar_canciones(nodo.derecha)

        # Iniciar búsqueda desde la raíz del árbol
        buscar_canciones(self.arbol.raiz)

        # Limpiar la lista
        self.resultList.clear()

        # Llenar la lista con los resultados filtrados
        for track_name, artist_name, genre, year, duration_ms, popularity in results:
            duration = f"{duration_ms // 60000}:{(duration_ms % 60000) // 1000:02d}"
            item_text = f"Canción: {track_name} - Artista: {artist_name} - Género: {genre} - Año: {year} - Popularidad: {popularity}"
            self.resultList.addItem(item_text)

    def addToPlaylist(self):
        selected_items = self.resultList.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, seleccione al menos una canción.')
            return

        for item in selected_items:
            # Extraer información de la canción del texto del item
            parts = item.text().split(' - ')
            track_name = parts[0].replace('Canción: ', '').strip()
            artist_name = parts[1].replace('Artista: ', '').strip()

            # Buscar la canción en el BST
            clave = (artist_name, track_name)
            detalles = self.arbol.buscar(clave)

            if detalles:
                year = detalles['year']
                duration_ms = detalles['duration_ms']
                popularity = detalles['popularity']  # Obtener popularidad

                # Convertir la duración de milisegundos a minutos y segundos
                duration = f"{duration_ms // 60000}:{(duration_ms % 60000) // 1000:02d}"

                # Crear un objeto Cancion y añadirlo a la lista de reproducción
                cancion = Cancion(track_name, artist_name, year, duration, popularity)
                self.gestor.agregar_cancion(cancion)
                print(f"Agregada a la playlist: {item.text()}")  # Para depuración

        QMessageBox.information(self, 'Éxito', 'Canciones añadidas a la playlist.')

    def showPlaylist(self):
        self.playlistWindow = VentanaPlaylist(self.gestor, self)
        self.playlistWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VentanaPrincipal()
    ex.show()
    sys.exit(app.exec_())
