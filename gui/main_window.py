from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from gui.pages.bleed_page import BleedPage

class ECAMWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A320neo ECAM Simulator")
        self.setGeometry(100, 100, 800, 600)

        # Create tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add tabs for different system pages
        self.bleed_tab = BleedPage()  # Bleed page
        self.tabs.addTab(self.bleed_tab, "BLEED")