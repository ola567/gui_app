from PyQt5 import QtCore, QtGui, QtWidgets


class TaskView(object):
    def setup_view(self, add_task):
        add_task.setObjectName("add_task")
        add_task.resize(600, 800)
        add_task.setStyleSheet("background-color: rgb(217, 217, 217);\n")
        self.add_task_label = QtWidgets.QLabel(add_task)
        self.add_task_label.setGeometry(QtCore.QRect(0, 0, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.add_task_label.setFont(font)
        self.add_task_label.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "text-align: center;\n"
                                          "border-radius: 10px;")
        self.add_task_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add_task_label.setObjectName("add_task_label")
        self.ok_button = QtWidgets.QPushButton(add_task)
        self.ok_button.setGeometry(QtCore.QRect(20, 700, 270, 50))
        self.ok_button.setStyleSheet("background-color: rgb(86, 205, 14);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 10px;")
        self.ok_button.setObjectName("ok_button")
        self.finish_date_label = QtWidgets.QLabel(add_task)
        self.finish_date_label.setGeometry(QtCore.QRect(20, 450, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.finish_date_label.setFont(font)
        self.finish_date_label.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "text-align: center;\n"
                                             "border-radius: 10px;")
        self.finish_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.finish_date_label.setObjectName("finish_date_label")
        self.content_value = QtWidgets.QPlainTextEdit(add_task)
        self.content_value.setGeometry(QtCore.QRect(20, 290, 560, 121))
        self.content_value.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;")
        self.content_value.setObjectName("content_value")
        self.cancel_button = QtWidgets.QPushButton(add_task)
        self.cancel_button.setGeometry(QtCore.QRect(310, 700, 270, 50))
        self.cancel_button.setStyleSheet("background-color: rgb(192, 28, 40);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;")
        self.cancel_button.setObjectName("cancel_button")
        self.title_label = QtWidgets.QLabel(add_task)
        self.title_label.setGeometry(QtCore.QRect(20, 70, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "text-align: center;\n"
                                       "border-radius: 10px;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.content_label = QtWidgets.QLabel(add_task)
        self.content_label.setGeometry(QtCore.QRect(20, 230, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.content_label.setFont(font)
        self.content_label.setStyleSheet("background-color: rgb(82, 95, 207);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "text-align: center;\n"
                                         "border-radius: 10px;")
        self.content_label.setAlignment(QtCore.Qt.AlignCenter)
        self.content_label.setObjectName("content_label")
        self.title_input = QtWidgets.QPlainTextEdit(add_task)
        self.title_input.setGeometry(QtCore.QRect(20, 130, 560, 50))
        self.title_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;")
        self.title_input.setObjectName("title_input")
        self.finish_date_input = QtWidgets.QPlainTextEdit(add_task)
        self.finish_date_input.setGeometry(QtCore.QRect(20, 510, 560, 50))
        self.finish_date_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10px;")
        self.finish_date_input.setObjectName("finish_date_input")

        self.retranslate_view(add_task)
        QtCore.QMetaObject.connectSlotsByName(add_task)

    def retranslate_view(self, add_task):
        _translate = QtCore.QCoreApplication.translate
        add_task.setWindowTitle(_translate("add_task", "Dodaj zadanie"))
        self.add_task_label.setText(_translate("add_task", "Dodaj zadanie"))
        self.ok_button.setText(_translate("add_task", "Ok"))
        self.finish_date_label.setText(_translate("add_task", "Data ukończenia"))
        self.cancel_button.setText(_translate("add_task", "Anuluj"))
        self.title_label.setText(_translate("add_task", "Tytuł"))
        self.content_label.setText(_translate("add_task", "Treść"))
