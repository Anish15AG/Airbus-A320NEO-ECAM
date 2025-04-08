from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from core.bleed import BleedSystem
from PyQt5.QtCore import QTimer

class BleedPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Title
        title_label = QLabel("BLEED DATA")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(title_label)

        # Labels for displaying data
        self.temp_lo_label = QLabel()
        self.temp_hi_label = QLabel()
        self.pressure_label = QLabel()

        self.layout.addWidget(self.temp_lo_label)
        self.layout.addWidget(self.temp_hi_label)
        self.layout.addWidget(self.pressure_label)

        # Simulate Bleed System
        self.bleed_system = BleedSystem()
        self.update_data()  # Display initial data

        # Timer for real-time updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # Update every 1 second

    def update_data(self):
        """Update the displayed data with the latest simulation values."""
        data = self.bleed_system.get_data()
        self.temp_lo_label.setText(f"Temperature LO: {data['Temperature LO']:.1f} °C")
        self.temp_hi_label.setText(f"Temperature HI: {data['Temperature HI']:.1f} °C")
        self.pressure_label.setText(f"Pressure: {data['Pressure']:.1f} PSI")

        # Generate new data
        self.bleed_system.update()