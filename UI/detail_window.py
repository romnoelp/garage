from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFrame
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import os

class DetailWindow(QWidget):
    def __init__(self, motorcycle):
        super().__init__()
        self.motorcycle = motorcycle
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.motorcycle.brand)
        self.resize(650, 600)
        self.center_window()

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Image Container (Rounded Borders)
        image_frame = QFrame(self)
        image_frame.setObjectName("image_container")  # ✅ Style the entire container
        image_layout = QVBoxLayout(image_frame)

        # Image Label
        self.image_label = QLabel(self)
        self.image_label.setObjectName("image_label")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ✅ Load image from local file instead of URL
        image_path = self.get_image_path(self.motorcycle.brand)
        pixmap = self.load_image(image_path)
        if pixmap:
            self.image_label.setPixmap(pixmap.scaled(500, 250))
        else:
            print(f"Error: Image not found for {self.motorcycle.brand}")

        image_layout.addWidget(self.image_label)
        layout.addWidget(image_frame)

        # Frame for details
        detail_frame = QFrame()
        detail_frame.setObjectName("detail_frame")
        detail_layout = QVBoxLayout(detail_frame)

        # Details Label (Includes Specific Features)
        self.details_label = QLabel(self.get_motorcycle_details(), self)
        self.details_label.setObjectName("details_label")
        self.details_label.setFont(QFont("Arial", 14))
        detail_layout.addWidget(self.details_label)

        layout.addWidget(detail_frame)

        # Transmission Toggle Button (For Honda Rebel 1100)
        if hasattr(self.motorcycle, "switch_transmission"):
            self.toggle_transmission_button = QPushButton("Switch Transmission", self)
            self.toggle_transmission_button.setObjectName("toggle_button")
            self.toggle_transmission_button.clicked.connect(self.switch_transmission)
            layout.addWidget(self.toggle_transmission_button)

        # Back Button
        self.back_button = QPushButton("Back", self)
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.go_back_to_main_menu)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def switch_transmission(self):
        """Switch transmission for Honda Rebel 1100"""
        self.motorcycle.switch_transmission()
        self.details_label.setText(self.get_motorcycle_details())  # Update details

    def get_motorcycle_details(self):
        """Generate details dynamically"""
        details = f"Engine: {self.motorcycle.engine_cc}cc\n"
        details += f"Valves: {self.motorcycle.valve_count}\n"

        if hasattr(self.motorcycle, "is_dct"):
            details += f"Transmission: {'DCT (Automatic)' if self.motorcycle.is_dct else 'Manual'}\n"
            details += f"Cruiser Style: {'Yes' if self.motorcycle.cruiser_style else 'No'}\n"
            details += f"Torque Control: {'Yes' if self.motorcycle.torque_control else 'No'}\n"

        if hasattr(self.motorcycle, "off_road_capable"):
            details += f"Transmission: Automatic\n"
            details += f"Off-Road Capable: {'Yes' if self.motorcycle.off_road_capable else 'No'}\n"
            details += f"Keyless Ignition: {'Yes' if self.motorcycle.keyless_ignition else 'No'}\n"

        return details

    def get_image_path(self, brand):
        """Returns the correct local image path based on the motorcycle brand"""
        images = {
            "Honda Rebel 1100": "Images/rebel.jpg",
            "Honda ADV 160": "Images/adv.jpg",
        }
        
        path = images.get(brand)
        if not path or not os.path.exists(path):  
            print(f"Warning: No image found for {brand}, using default image.")
            return "Images/default.jpg"  
        
        return path

    def go_back_to_main_menu(self):
        """ Closes the detail window and reopens the main menu """
        from UI.main_menu import MainMenu
        self.close()
        self.main_menu = MainMenu()
        self.main_menu.show()

    def load_image(self, path):
        """ Loads an image from a local file path """
        image = QPixmap(path)
        if not image.isNull():
            return image
        else:
            print(f"Error: Failed to load image from {path}")
            return None

    def center_window(self):
        screen_geometry = self.screen().availableGeometry()
        self.move(screen_geometry.center() - self.rect().center())
