from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont
from UI.detail_window import DetailWindow
from Implementation.honda_rebel import HondaRebel1100
from Implementation.adv import ADV

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Inheritance Showcase")
        self.resize(500, 200)
        self.center_window()

        layout = QVBoxLayout()

        self.title_label = QLabel("Choose a Scooter Type:", self)
        self.title_label.setObjectName("title_label")
        self.title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout.addWidget(self.title_label)

        self.manual_button = QPushButton("Honda Rebel 1100", self)
        self.automatic_button = QPushButton("Honda ADV 160", self)

        self.manual_button.clicked.connect(lambda: self.open_new_window(HondaRebel1100()))
        self.automatic_button.clicked.connect(lambda: self.open_new_window(ADV(160, 4)))  

        layout.addWidget(self.manual_button)
        layout.addWidget(self.automatic_button)
        self.setLayout(layout)

    def open_new_window(self, motorcycle):
        """ Closes the main window and opens a new detail window """
        self.close()
        self.detail_window = DetailWindow(motorcycle) 
        self.detail_window.show()

    def center_window(self):
        """ Centers the window on the screen """
        screen_geometry = self.screen().availableGeometry()
        self.move(screen_geometry.center() - self.rect().center())
