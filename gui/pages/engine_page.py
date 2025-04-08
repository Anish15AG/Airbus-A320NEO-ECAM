from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from core.engine import EngineSystem

class EngPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Title
        title_label = QLabel("ENGINE DATA")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(title_label)

        # Labels for displaying data
        self.n1_label = QLabel()
        self.n2_label = QLabel()
        self.oil_pressure_label = QLabel()
        self.oil_temperature_label = QLabel()
        self.egt_label = QLabel()  # New label for EGT

        self.layout.addWidget(self.n1_label)
        self.layout.addWidget(self.n2_label)
        self.layout.addWidget(self.oil_pressure_label)
        self.layout.addWidget(self.oil_temperature_label)
        self.layout.addWidget(self.egt_label)  # Add EGT label to layout

        # Simulate Engine System
        self.engine_system = EngineSystem()
        self.update_data()  # Display initial data

        # Timer for real-time updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # Update every 1 second

    def update_data(self):
        """Update the displayed data with the latest simulation values."""
        data = self.engine_system.get_data()
        self.n1_label.setText(f"N1: {data['N1']:.1f}%")
        self.n2_label.setText(f"N2: {data['N2']:.1f}%")
        self.oil_pressure_label.setText(f"Oil Pressure: {data['Oil Pressure']:.1f} PSI")
        self.oil_temperature_label.setText(f"Oil Temperature: {data['Oil Temperature']:.1f} °C")
        self.egt_label.setText(f"EGT: {data['EGT']:.1f} °C")  # Update EGT label

        # Generate new data
        self.engine_system.update()