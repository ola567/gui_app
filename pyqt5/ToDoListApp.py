from PyQt5 import QtCore, QtGui, QtWidgets

from MainView import MainView


class ToDoListAppView(object):
    def setup_view(self, ToDoListApp):
        self.ToDoListApp = ToDoListApp
        self.ToDoListApp.setObjectName("ToDoListApp")
        self.ToDoListApp.resize(600, 800)
        self.ToDoListApp.setStyleSheet("background-color: rgb(82, 95, 207)")
        self.centralwidget = QtWidgets.QWidget(self.ToDoListApp)
        self.centralwidget.setObjectName("centralwidget")

        self.app_name = QtWidgets.QLabel(self.centralwidget)
        self.app_name.setGeometry(QtCore.QRect(260, 320, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet("color: rgb(255, 255, 255)")
        self.app_name.setObjectName("app_name")

        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(150, 510, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet(
            '''
            background-color: rgb(239, 139, 235);
            color: rgb(255, 255, 255);
            border-radius: 10px;
            }
            *:hover{
                background-color: rgb(229, 129, 225);
            }
            '''
        )
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.start_app)
        self.main_view_handler = None

        self.app_icon = QtWidgets.QLabel(self.centralwidget)
        self.app_icon.setGeometry(QtCore.QRect(40, 260, 201, 201))
        self.app_icon.setObjectName("app_icon")

        self.ToDoListApp.setCentralWidget(self.centralwidget)

        self.retranslate_view(self.ToDoListApp)
        QtCore.QMetaObject.connectSlotsByName(self.ToDoListApp)

    def retranslate_view(self, ToDoListApp):
        _translate = QtCore.QCoreApplication.translate
        ToDoListApp.setWindowTitle(_translate("ToDoListApp", "Lista zadań"))
        self.app_name.setText(_translate("ToDoListApp", "Lista zadań"))
        self.start_button.setText(_translate("ToDoListApp", "Start"))
        self.app_icon.setText(
            _translate("ToDoListApp", "<html><head/><body><p><img src=\"img/app_icon.png\"/></p></body></html>"))

    def start_app(self):
        if self.main_view_handler is None:
            self.main_view_window = QtWidgets.QMainWindow()
            self.main_view_handler = MainView()
            self.main_view_handler.setup_view(self.main_view_window)
            self.main_view_window.show()
            self.ToDoListApp.close()
        else:
            self.main_view_window.show()
            self.ToDoListApp.close()
