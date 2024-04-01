import sys

from PyQt5 import QtWidgets

from ToDoListApp import ToDoListAppView


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app_window = QtWidgets.QMainWindow()
    ui = ToDoListAppView()
    ui.setup_view(app_window)
    app_window.show()
    sys.exit(app.exec_())

