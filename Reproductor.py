from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize, QTimer
import random

class Reproductor(QWidget):
    def __init__(self, gestor, parent=None):
        super().__init__(parent)
        self.gestor = gestor  # Asegúrate de que esto es una instancia de GestorMusica
        self.cancion_actual = None
        self.nodo_actual = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_progreso)
        self.initUI()

    def initUI(self):
        # Configurar la ventana
        self.setWindowTitle('Reproductor de Música')
        self.setGeometry(300, 300, 400, 250)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        
        # Layout principal
        layout = QVBoxLayout()
        
        # Imagen de la canción (placeholder)
        self.imageLabel = QLabel(self)
        self.imageLabel.setPixmap(QPixmap('img/music.png').scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.imageLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.imageLabel)
        
        # Datos de la canción
        self.infoLabel = QLabel('', self)
        layout.addWidget(self.infoLabel)

        # Información de tiempo
        self.timeLabel = QLabel('00:00 / 00:00', self)
        layout.addWidget(self.timeLabel)
        
        # Barra de progreso
        self.progressSlider = QSlider(Qt.Horizontal, self)
        self.progressSlider.setRange(0, 100)  # Ajusta el rango según la duración de la canción
        layout.addWidget(self.progressSlider)
        
        # Controles de reproducción
        controlLayout = QHBoxLayout()
        
        self.retrocederButton = QPushButton()
        self.retrocederButton.setIcon(QIcon('img/retroceder.png'))
        self.retrocederButton.setIconSize(QSize(30, 30))
        controlLayout.addWidget(self.retrocederButton)
        
        self.pausarButton = QPushButton()
        self.pausarButton.setIcon(QIcon('img/pausa.png'))
        self.pausarButton.setIconSize(QSize(30, 30))
        controlLayout.addWidget(self.pausarButton)

        self.reproducirButton = QPushButton()
        self.reproducirButton.setIcon(QIcon('img/reproducir.png'))
        self.reproducirButton.setIconSize(QSize(30, 30))
        controlLayout.addWidget(self.reproducirButton)
        
        self.adelantarButton = QPushButton()
        self.adelantarButton.setIcon(QIcon('img/adelantar.png'))
        self.adelantarButton.setIconSize(QSize(30, 30))
        controlLayout.addWidget(self.adelantarButton)
        
        layout.addLayout(controlLayout)
        
        self.setLayout(layout)

        # Conectar señales
        self.retrocederButton.clicked.connect(self.retroceder)
        self.pausarButton.clicked.connect(self.pausar)
        self.reproducirButton.clicked.connect(self.reproducir)
        self.adelantarButton.clicked.connect(self.adelantar)

    def actualizar_info(self, cancion):
        self.cancion_actual = cancion
        self.infoLabel.setText(f"{self.cancion_actual.titulo} - {self.cancion_actual.artista}")
        # Actualizar la imagen de la canción si tienes una fuente de imagen adecuada
        
        if self.cancion_actual:
            self.progressSlider.setRange(0, self.cancion_actual.duracion_ms // 1000)  # Supone duración en milisegundos
            self.timeLabel.setText(f"00:00 / {self.formatear_duracion(self.cancion_actual.duracion_ms // 1000)}")

    def reproducir(self):
        if not self.cancion_actual:
            # Seleccionar una canción aleatoria como la actual
            canciones = self.gestor.obtener_lista()
            if canciones:
                self.cancion_actual = random.choice(canciones)
                self.nodo_actual = self.gestor.lista_canciones.buscar_nodo(self.cancion_actual.titulo)
                self.actualizar_info(self.cancion_actual)
                self.timer.start(1000)  # Actualizar cada segundo

    def pausar(self):
        self.timer.stop()  # Detener la actualización de la barra de progreso

    def retroceder(self):
        if self.nodo_actual and self.nodo_actual.anterior:
            self.nodo_actual = self.nodo_actual.anterior
            self.cancion_actual = self.nodo_actual.cancion
            self.actualizar_info(self.cancion_actual)
            # Lógica adicional para retroceder la reproducción (si es necesario)

    def adelantar(self):
        if self.nodo_actual and self.nodo_actual.siguiente:
            self.nodo_actual = self.nodo_actual.siguiente
            self.cancion_actual = self.nodo_actual.cancion
            self.actualizar_info(self.cancion_actual)
            # Lógica adicional para adelantar la reproducción (si es necesario)

    def actualizar_progreso(self):
        if self.cancion_actual:
            # Simular la actualización de la barra de progreso
            current_value = self.progressSlider.value()
            new_value = min(current_value + 1, self.progressSlider.maximum())
            self.progressSlider.setValue(new_value)
            # Actualizar la etiqueta de tiempo
            self.timeLabel.setText(f"{self.formatear_duracion(current_value)} / {self.formatear_duracion(self.progressSlider.maximum())}")

    def formatear_duracion(self, segundos):
        minutos, segundos = divmod(segundos, 60)
        return f"{minutos:02}:{segundos:02}"
