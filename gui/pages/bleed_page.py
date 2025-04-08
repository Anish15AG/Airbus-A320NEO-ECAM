from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from core.bleed import BleedSystem

class BleedPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Title
        title_label = QLabel("BLEED DATA")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(title_label)

        # Simulate Bleed System
        self.bleed_system = BleedSystem()
        self.bleed_system.update()  # Generate initial data

        # Display Bleed System data
        self.temp_lo_label = QLabel()
        self.temp_hi_label = QLabel()
        self.pressure_label = QLabel()

        self.layout.addWidget(self.temp_lo_label)
        self.layout.addWidget(self.temp_hi_label)
        self.layout.addWidget(self.pressure_label)

        self.update_data()

    def update_data(self):
        """Update the displayed data with the latest simulation values."""
        data = self.bleed_system.get_data()
        self.temp_lo_label.setText(f"Temperature LO: {data['Temperature LO']:.1f} °C")
        self.temp_hi_label.setText(f"Temperature HI: {data['Temperature HI']:.1f} °C")
        self.pressure_label.setText(f"Pressure: {data['Pressure']:.1f} PSI")

        # Schedule the next update
        self.bleed_system.update()