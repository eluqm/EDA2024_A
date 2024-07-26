import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QMainWindow, QApplication, QMenu, QAction
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
from Reproductor import Reproductor
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
        
         # Menú de opciones de ordenamiento
        self.sortMenu = QMenu(self)
        
        # Crear acciones para cada criterio de ordenamiento
        self.sortPopularityAction = QAction('Popularidad', self)
        self.sortYearAction = QAction('Año', self)
        self.sortDurationAction = QAction('Duración', self)
        
        # Añadir acciones al menú
        self.sortMenu.addAction(self.sortPopularityAction)
        self.sortMenu.addAction(self.sortYearAction)
        self.sortMenu.addAction(self.sortDurationAction)
        
        # Conectar las acciones a los métodos correspondientes
        self.sortPopularityAction.triggered.connect(lambda: self.ordenarLista('popularity'))
        self.sortYearAction.triggered.connect(lambda: self.ordenarLista('year'))
        self.sortDurationAction.triggered.connect(lambda: self.ordenarLista('duration'))
        
        # Asignar el menú al botón
        self.sortButton.setMenu(self.sortMenu)

        self.lista_canciones_ui = QListWidget(self)

        # Layout para los botones
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.playButton)
        buttonLayout.addWidget(self.removeButton)
        buttonLayout.addWidget(self.sortButton)
        buttonLayout.addWidget(self.closeButton)
        
        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Playlist', self))
        layout.addWidget(self.lista_canciones_ui)
        layout.addLayout(buttonLayout)
        
        self.centralWidget.setLayout(layout)
        
        # Configurar la ventana principal
        self.setWindowTitle('Lista de Reproducción')
        self.setGeometry(200, 200, 600, 400)  # Ajustar el tamaño de la ventana
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon('img/icon.png'))  # Si tienes un icono
        
        # Conectar señales
        self.closeButton.clicked.connect(self.close)
        self.removeButton.clicked.connect(self.removeSelectedItem)
        self.playButton.clicked.connect(self.reproducirAleatorio)
        
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
        self.lista_canciones_ui.clear()
        for cancion in self.gestor.obtener_lista():
            item_text = f"Canción: {cancion.titulo} - Artista: {cancion.artista} - Año: {cancion.año} - Popularidad: {cancion.popularidad}"
            self.lista_canciones_ui.addItem(item_text)

    def removeSelectedItem(self):
        selected_items = self.lista_canciones_ui.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            title = item.text().split(' - ')[0]  # Asume que el formato es 'Título - Artista'
            self.lista_canciones_ui.takeItem(self.lista_canciones_ui.row(item))
            self.gestor.eliminar_cancion(title)
    
    def reproducirAleatorio(self):
        canciones = self.gestor.reproduccion_aleatoria()
        if canciones:
            cancion = canciones[0]  # Reproduce la primera canción seleccionada
            self.reproductorDialog = Reproductor(cancion, self)
            self.reproductorDialog.show()

            # Configurar el temporizador para actualizar la barra de progreso (simulación)
            self.timer = QTimer()
            self.timer.timeout.connect(self.actualizar_progreso)
            self.timer.start(1000)  # Actualiza cada segundo

    def actualizar_progreso(self):
        if self.reproductorDialog:
            # Simular la actualización de la barra de progreso
            current_value = self.reproductorDialog.progressSlider.value()
            new_value = min(current_value + 1, self.reproductorDialog.progressSlider.maximum())
            self.reproductorDialog.progressSlider.setValue(new_value)

    def ordenarLista(self, criterio):
        self.gestor.ordenar_lista(criterio)
        self.actualizar_lista()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestor = GestorMusica()
    window = VentanaPlaylist(gestor)
    window.show()
    sys.exit(app.exec_())
