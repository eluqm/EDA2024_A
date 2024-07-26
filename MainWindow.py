import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from gestor import GestorMusica
from cancion import Cancion

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reproductor de musica")
        self.setGeometry(100, 100, 600, 300)

        mainLayout = QVBoxLayout()

        headerLayout = QHBoxLayout()
        headerLayout.setContentsMargins(10, 10, 10, 10)

        userIcon = QLabel()
        pixmap = QPixmap('img/usericon.png').scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        userIcon.setPixmap(pixmap)

        userName = QLabel('Estructura de datos y algoritmos')
        userName.setStyleSheet("font-size: 18px; margin-left: 10px;")

        headerLayout.addWidget(userIcon)
        headerLayout.addWidget(userName)
        headerLayout.addStretch()

        mainLayout.addLayout(headerLayout)

        #botones
        buttonLayout = QVBoxLayout()
        playMusicButton = QPushButton('Reproducir Música')
        orderByPopularityButton = QPushButton('Ordenar por Popularidad')
        orderByYearButton = QPushButton('Ordenar por Año')
        orderByDurationButton = QPushButton('Ordenar por Duración')
        addSongButton = QPushButton('Agregar Canción')

        buttonLayout.addWidget(playMusicButton)
        buttonLayout.addWidget(orderByPopularityButton)
        buttonLayout.addWidget(orderByYearButton)
        buttonLayout.addWidget(orderByDurationButton)
        buttonLayout.addWidget(addSongButton)

        mainLayout.addLayout(buttonLayout)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

        #estilos
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px;
                margin: 5px;
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QLabel {
                color: #333;
            }
        """)

