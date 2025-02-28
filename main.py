import sys
from PyQt6.QtWidgets import QApplication
from UI.main_menu import MainMenu

def load_stylesheet():
    """Loads the styles.qss file"""
    with open("styles.qss", "r") as file:
        return file.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet())  
    main_window = MainMenu()
    main_window.show()
    sys.exit(app.exec())
