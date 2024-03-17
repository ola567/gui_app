import sys

from PyQt5 import QtWidgets

from ToDoListApp import ToDoListAppUI


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ToDoListApp = QtWidgets.QMainWindow()
    ui = ToDoListAppUI()
    ui.setupUi(ToDoListApp)
    ToDoListApp.show()
    sys.exit(app.exec_())
