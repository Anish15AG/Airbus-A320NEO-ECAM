import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import ECAMWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ECAMWindow()
    window.show()
    sys.exit(app.exec_())