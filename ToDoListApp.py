from PyQt5 import QtCore, QtGui, QtWidgets


class ToDoListAppUI(object):
    def setupUi(self, ToDoListApp):
        ToDoListApp.setObjectName("ToDoListApp")
        ToDoListApp.resize(600, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_files/../img/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ToDoListApp.setWindowIcon(icon)
        ToDoListApp.setStyleSheet("background-color: rgb(82, 95, 207)")
        self.centralwidget = QtWidgets.QWidget(ToDoListApp)
        self.centralwidget.setObjectName("centralwidget")
        self.app_name = QtWidgets.QLabel(self.centralwidget)
        self.app_name.setGeometry(QtCore.QRect(260, 320, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet("color: rgb(255, 255, 255)")
        self.app_name.setObjectName("app_name")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(150, 510, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("background-color: rgb(239, 139, 235);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px")
        self.start_button.setObjectName("start_button")
        self.app_icon = QtWidgets.QLabel(self.centralwidget)
        self.app_icon.setGeometry(QtCore.QRect(40, 260, 201, 201))
        self.app_icon.setObjectName("app_icon")
        ToDoListApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(ToDoListApp)
        QtCore.QMetaObject.connectSlotsByName(ToDoListApp)

    def retranslateUi(self, ToDoListApp):
        _translate = QtCore.QCoreApplication.translate
        ToDoListApp.setWindowTitle(_translate("ToDoListApp", "Lista zadań"))
        self.app_name.setText(_translate("ToDoListApp", "Lista zadań"))
        self.start_button.setText(_translate("ToDoListApp", "Start"))
        self.app_icon.setText(
            _translate("ToDoListApp", "<html><head/><body><p><img src=\"img/app_icon.png\"/></p></body></html>"))
