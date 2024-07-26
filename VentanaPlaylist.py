import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from gestor import GestorMusica

class VentanaPlaylist(QMainWindow):
    def __init__(self, gestor, parent=None):
        super().__init__(parent)
        self.gestor = gestor
        self.initUI()
        self.actualizar_lista()

    def initUI(self):
        # Crear los elementos de la interfaz
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        self.playlistList = QListWidget(self)
        
        self.playButton = QPushButton('Reproducir Aleatorio', self)
        self.closeButton = QPushButton('Cerrar', self)
        self.removeButton = QPushButton('Eliminar Canción', self)
        self.sortButton = QPushButton('Ordenar', self)
        
        # Layout para los botones
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.playButton)
        buttonLayout.addWidget(self.removeButton)
        buttonLayout.addWidget(self.sortButton)
        buttonLayout.addWidget(self.closeButton)
        
        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Playlist', self))
        layout.addWidget(self.playlistList)
        layout.addLayout(buttonLayout)
        
        self.centralWidget.setLayout(layout)
        
        # Configurar la ventana principal
        self.setWindowTitle('Lista de Reproducción')
        self.setGeometry(200, 200, 400, 300)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon('img/icon.png'))  # Si tienes un icono
        
        # Conectar señales
        self.closeButton.clicked.connect(self.close)
        self.removeButton.clicked.connect(self.removeSelectedItem)
        self.playButton.clicked.connect(self.reproducirAleatorio)
        self.sortButton.clicked.connect(self.ordenarLista)
        
        self.applyStyles()

    def applyStyles(self):
        # Estilo para los botones y la lista
        styleSheet = """
        QWidget {
            background-color: #f0f0f0;
        }
        QLabel {
            color: #333;
            font-size: 18px;
            font-weight: bold;
        }
        QListWidget {
            padding: 10px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: white;
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
        """
        self.setStyleSheet(styleSheet)

    def actualizar_lista(self):
        self.playlistList.clear()
        canciones = self.gestor.obtener_lista()
        print(f"Lista de canciones: {canciones}")  # Para depuración
        for cancion in canciones:
            self.playlistList.addItem(f"{cancion.titulo} - {cancion.artista}")

    def removeSelectedItem(self):
        selected_items = self.playlistList.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            title = item.text().split(' - ')[0]  # Asume que el formato es 'Título - Artista'
            self.playlistList.takeItem(self.playlistList.row(item))
            self.gestor.eliminar_cancion(title)
    
    def reproducirAleatorio(self):
        canciones = self.gestor.reproduccion_aleatoria()
        for cancion in canciones:
            print(f"Reproduciendo: {cancion.titulo} - {cancion.artista}")

    def ordenarLista(self):
        self.gestor.ordenar_lista('popularity')  # Ordenar por popularidad
        self.actualizar_lista()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestor = GestorMusica()
    window = VentanaPlaylist(gestor)
    window.show()
    sys.exit(app.exec_())
