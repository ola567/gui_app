import sys

from PyQt5.QtWidgets import QApplication

from start_app import StartApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartApp()
    window.show()
    sys.exit(app.exec_())
