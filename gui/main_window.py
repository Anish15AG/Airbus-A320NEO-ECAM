from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class ECAMWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A320neo ECAM Simulator")
        self.setGeometry(100, 100, 800, 600)

        #Create a Tab Widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        #Add tab for different System Pages
        self.eng_tab = QWidget()
        self.bleed_tab = QWidget()
        self.cab_press_tab = QWidget()

        self.tabs.addTab(self.eng_tab, "ENG")
        self.tabs.addTab(self.bleed_tab, "BLEED")
        self.tabs.addTab(self.cab_press_tab, "CAB PRESS")

        # Set up BLEED tab
        bleed_layout = QVBoxLayout()
        bleed_label = QLabel("BLEED DATA")
        bleed_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        bleed_layout.addWidget(bleed_label)
        self.bleed_tab.setLayout(bleed_layout)

        # Set up CAB PRESS tab
        cab_press_layout = QVBoxLayout()
        cab_press_label = QLabel("CABIN PRESSURIZATION DATA")
        cab_press_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        cab_press_layout.addWidget(cab_press_label)
        self.cab_press_tab.setLayout(cab_press_layout)