from PyQt5 import QtCore, QtGui, QtWidgets


class AboutAppView(object):
    def setup_view(self, about_app_window):
        about_app_window.setObjectName("about_app_window")
        about_app_window.resize(600, 230)
        about_app_window.setStyleSheet("background-color: rgb(217, 217, 217)")
        self.centralwidget = QtWidgets.QWidget(about_app_window)
        self.centralwidget.setObjectName("centralwidget")
        self.about_app_label = QtWidgets.QLabel(self.centralwidget)
        self.about_app_label.setGeometry(QtCore.QRect(0, 0, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.about_app_label.setFont(font)
        self.about_app_label.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "text-align: center;\n"
                                           "border-radius: 10px;")
        self.about_app_label.setAlignment(QtCore.Qt.AlignCenter)
        self.about_app_label.setObjectName("about_app_label")

        self.about_app_content = QtWidgets.QLabel(self.centralwidget)
        self.about_app_content.setGeometry(QtCore.QRect(20, 70, 560, 140))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.about_app_content.setFont(font)
        self.about_app_content.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "text-align: center;\n"
                                             "border-radius: 10px;\n"
                                             "padding: 30px;")
        self.about_app_content.setWordWrap(True)
        self.about_app_content.setObjectName("about_app_content")
        about_app_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(about_app_window)
        QtCore.QMetaObject.connectSlotsByName(about_app_window)

    def retranslateUi(self, about_app_window):
        _translate = QtCore.QCoreApplication.translate
        about_app_window.setWindowTitle(_translate("about_app_window", "O aplikacji"))
        self.about_app_label.setText(_translate("about_app_window", "O aplikacji"))
        self.about_app_content.setText(_translate("about_app_window",
                                                  "Aplikacja umożliwia stworzenie listy zadań do zrobienia. Zadania można "
                                                  "dodawać, edytować, usuwać, oznaczać jako zrobione i nie zrobione. Oprócz "
                                                  "tego listę można zapisać w pliku tekstowym, jak również wczytać z pliku."))
