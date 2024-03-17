import sys

from PyQt5 import QtWidgets

from ToDoListApp import ToDoListAppView


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app_window = ToDoListAppView()
    app_window.show()
    sys.exit(app.exec_())
